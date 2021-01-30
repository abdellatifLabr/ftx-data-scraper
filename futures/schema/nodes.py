import graphene
from graphene_django.types import DjangoObjectType

from ..models import Spread, Future
from ..filters import SpreadFilterSet, FutureFilterSet


class SpreadNode(DjangoObjectType):
    pk = graphene.Int(source='pk')
    name = graphene.String(source='name')

    class Meta:
        model = Spread
        filterset_class = SpreadFilterSet
        interfaces = (graphene.relay.Node,)


class FutureNode(DjangoObjectType):
    class Meta:
        model = Future
        filterset_class = FutureFilterSet
        interfaces = (graphene.relay.Node,)
