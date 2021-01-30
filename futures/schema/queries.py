import graphene
from graphene_django.filter import DjangoFilterConnectionField

from .nodes import SpreadNode, FutureNode


class SpreadQuery(graphene.ObjectType):
    spread = graphene.relay.Node.Field(SpreadNode)
    spreads = DjangoFilterConnectionField(SpreadNode)


class FutureQuery(graphene.ObjectType):
    future = graphene.relay.Node.Field(FutureNode)
    futures = DjangoFilterConnectionField(FutureNode)
