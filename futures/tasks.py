import json
import urllib.request
from celery import shared_task

from .models import Future
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
