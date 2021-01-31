import json
import urllib.request
from celery import shared_task
from django.db.models import Q

from .models import Future, Spread, Pair
from .utils import snake_case


FTX_API_ENDPOINT = 'http://ftx.com/api'
USER_AGENT = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7)Gecko/2009021910 Firefox/3.0.7'


def request_json_data(url):
    headers = {'User-Agent': USER_AGENT}
    request = urllib.request.Request(url, None, headers)
    response = urllib.request.urlopen(request)
    content = response.read()
    json_content = json.loads(content)
    return json_content


def calculate_buy_spread(ask_a, bid_b):
    return (ask_a - bid_b) / (ask_a/2 + bid_b / 2)


def calculate_sell_spread(ask_b, bid_a):
    return (bid_a - ask_b) / (bid_a / 2 + ask_b / 2)


@shared_task
def get_futures_markets():
    url = f'{FTX_API_ENDPOINT}/futures'
    json_content = request_json_data(url)

    if json_content.get('success'):
        base_futures = json_content.get('result', [])

    for base_future in base_futures:
        # get stats
        name = base_future.get('name')
        stats_url = f'{FTX_API_ENDPOINT}/futures/{name}/stats'
        json_content = request_json_data(stats_url)
        if json_content.get('success'):
            stats = json_content.get('result', {})

        # merge stats with base future
        future = snake_case({**base_future, **stats})
        greeks = future.pop('greeks', None)
        if greeks:
            future = {**future, **greeks}

        try:
            _future = Future.objects.get(name=future.get('name'))

            for field, value in future.items():
                setattr(_future, field, value)

            _future.save()
        except Future.DoesNotExist:
            Future.objects.create(**future)

    # make combintions
    targeted_futures = Future.objects.only('name', 'underlying', 'ask', 'bid').filter(
        Q(
            Q(description__contains='Futures') or
            Q(description__contains='Perpetual')
        ) and
        ~Q(description__contains='Hashrate')
    )

    for i in range(targeted_futures.count()):
        for j in range(targeted_futures.count()):
            future_a = targeted_futures[i]
            future_b = targeted_futures[j]

            if future_a != future_b:
                if future_a.underlying == future_b.underlying:
                    if future_a.ask and future_a.bid and future_b.ask and future_b.bid:
                        buy_spread = calculate_buy_spread(future_a.ask, future_b.bid)
                        sell_spread = calculate_sell_spread(future_b.ask, future_a.bid)

                        pair, _ = Pair.objects.get_or_create(pair_a=future_a, pair_b=future_b)
                        Spread.objects.create(pair=pair, buy_spread=buy_spread, sell_spread=sell_spread)
