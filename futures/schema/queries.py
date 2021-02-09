from datetime import timedelta

import graphene
from django.db.models import Avg
from django.db.models.functions import Trunc
from django.utils import timezone
from graphene_django.filter import DjangoFilterConnectionField

from ..models import Pair
from .nodes import FutureNode, PairNode, SpreadNode
from .types import SpreadChartDataType


class SpreadQuery(graphene.ObjectType):
    spread = graphene.relay.Node.Field(SpreadNode)
    spreads = DjangoFilterConnectionField(SpreadNode)


class PairInput(graphene.InputObjectType):
    id = graphene.ID(required=True)
    buy_or_sell = graphene.String(required=True)


class SpreadChartQuery(graphene.ObjectType):
    chart_pairs_spreads = graphene.List(
        graphene.List(SpreadChartDataType),
        pairs_params=graphene.List(PairInput, required=True),
        time_frame=graphene.String(default_value='minute'),
        start_date=graphene.DateTime(),
        end_date=graphene.DateTime(default_value=timezone.now())
    )

    def resolve_chart_pairs_spreads(self, info, pairs_params, time_frame, end_date, start_date=None, **kwargs):
        data = []
        for pair_params in pairs_params:
            try:
                pair = Pair.objects.get(pk=pair_params.id)
            except Pair.DoesNotExist:
                continue

            spreads = pair.spreads.filter(created_at__range=[start_date or end_date - timedelta(days=10), end_date])
            is_buy = pair_params.buy_or_sell == 'buy'
            is_sell = pair_params.buy_or_sell == 'sell'

            if is_buy:
                chart_data = spreads.annotate(
                    timestamp=Trunc('created_at', time_frame)).values('timestamp').annotate(
                    buy_spread=Avg('buy_spread')).values(
                    'buy_spread', 'timestamp', 'pair').order_by('timestamp')

            if is_sell:
                chart_data = spreads.annotate(
                    timestamp=Trunc('created_at', time_frame)).values('timestamp').annotate(
                    sell_spread=Avg('sell_spread')).values(
                    'sell_spread', 'timestamp', 'pair').order_by('timestamp')

            data.append(chart_data)

        return data


class PairQuery(graphene.ObjectType):
    pair = graphene.relay.Node.Field(PairNode)
    pairs = DjangoFilterConnectionField(PairNode)


class FutureQuery(graphene.ObjectType):
    future = graphene.relay.Node.Field(FutureNode)
    futures = DjangoFilterConnectionField(FutureNode)
