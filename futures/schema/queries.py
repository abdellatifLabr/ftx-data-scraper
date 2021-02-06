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


class SpreadChartQuery(graphene.ObjectType):
    chart_spreads = graphene.List(
        SpreadChartDataType,
        pair_id=graphene.ID(required=True),
        time_frame=graphene.String(default_value='minute'),
        start_date=graphene.DateTime(),
        end_date=graphene.DateTime(default_value=timezone.now())
    )

    def resolve_chart_spreads(self, info, pair_id, time_frame, end_date, start_date=None, **kwargs):
        try:
            pair = Pair.objects.get(pk=pair_id)
        except Pair.DoesNotExist:
            raise Exception('This pair does not exist')

        spreads = pair.spreads.filter(created_at__range=[start_date or end_date - timedelta(days=10), end_date])
        data = spreads.annotate(
            timestamp=Trunc('created_at', time_frame)).values('timestamp').annotate(
            buy_spread=Avg('buy_spread'),
            sell_spread=Avg('sell_spread')).values(
            'buy_spread', 'sell_spread', 'timestamp').order_by('timestamp')

        return data


class PairQuery(graphene.ObjectType):
    pair = graphene.relay.Node.Field(PairNode)
    pairs = DjangoFilterConnectionField(PairNode)


class FutureQuery(graphene.ObjectType):
    future = graphene.relay.Node.Field(FutureNode)
    futures = DjangoFilterConnectionField(FutureNode)
