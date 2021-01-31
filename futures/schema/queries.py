import graphene
from graphene_django.filter import DjangoFilterConnectionField
from django.db.models.functions import TruncDay, TruncHour, TruncMinute
from django.db.models import Avg

from ..models import Pair
from .nodes import SpreadNode, FutureNode, PairNode
from .types import SpreadChartDataType


class SpreadQuery(graphene.ObjectType):
    spread = graphene.relay.Node.Field(SpreadNode)
    spreads = DjangoFilterConnectionField(SpreadNode)


class SpreadChartQuery(graphene.ObjectType):
    chart_spreads = graphene.List(
        SpreadChartDataType,
        pair_id=graphene.ID(required=True),
        time_frame=graphene.String(default_value='minute'),
        count=graphene.Int(default_value=20)
    )

    def resolve_chart_spreads(self, info, pair_id, time_frame, count, **kwargs):
        try:
            pair = Pair.objects.get(pk=pair_id)
        except Pair.DoesNotExist:
            raise Exception('This pair does not exist')

        spreads = pair.spreads.all()
        data = None
        if time_frame == 'minute':
            data = spreads.annotate(
                minute=TruncMinute('created_at')).values('minute').annotate(
                buy_spread=Avg('buy_spread'),
                sell_spread=Avg('sell_spread')).values(
                'buy_spread', 'sell_spread', 'minute').order_by('minute')[:count]

        elif time_frame == 'hour':
            data = spreads.annotate(
                hour=TruncHour('created_at')).values('hour').annotate(
                buy_spread=Avg('buy_spread'),
                sell_spread=Avg('sell_spread')).values(
                'buy_spread', 'sell_spread', 'hour').order_by('hour')[:count]

        elif time_frame == 'day':
            data = spreads.annotate(
                day=TruncDay('created_at')).values('day').annotate(
                buy_spread=Avg('buy_spread'),
                sell_spread=Avg('sell_spread')).values(
                'buy_spread', 'sell_spread', 'day').order_by('day')[:count]

        return data


class PairQuery(graphene.ObjectType):
    pair = graphene.relay.Node.Field(PairNode)
    pairs = DjangoFilterConnectionField(PairNode)


class FutureQuery(graphene.ObjectType):
    future = graphene.relay.Node.Field(FutureNode)
    futures = DjangoFilterConnectionField(FutureNode)
