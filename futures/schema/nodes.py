import graphene
from graphene_django.types import DjangoObjectType

from ..models import Spread, Future, Pair
from ..filters import SpreadFilterSet, FutureFilterSet


class SpreadNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    timestamp = graphene.DateTime(source='created_at')

    class Meta:
        model = Spread
        filterset_class = SpreadFilterSet
        interfaces = (graphene.relay.Node,)


class PairNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    name = graphene.String(source='name')

    class Meta:
        model = Pair
        filter_fields = {}
        interfaces = (graphene.relay.Node,)


class FutureNode(DjangoObjectType):
    pk = graphene.Int(source='pk')

    class Meta:
        model = Future
        filterset_class = FutureFilterSet
        interfaces = (graphene.relay.Node,)
