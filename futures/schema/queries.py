import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import SpreadNode, FutureNode, PairNode


class SpreadQuery(graphene.ObjectType):
    spread = graphene.relay.Node.Field(SpreadNode)
    spreads = DjangoFilterConnectionField(SpreadNode)


class PairQuery(graphene.ObjectType):
    pair = graphene.relay.Node.Field(PairNode)
    pairs = DjangoFilterConnectionField(PairNode)


class FutureQuery(graphene.ObjectType):
    future = graphene.relay.Node.Field(FutureNode)
    futures = DjangoFilterConnectionField(FutureNode)
