import graphene
import channels_graphql_ws

from ..models import Spread
from .nodes import SpreadNode


class SpreadSubscription(channels_graphql_ws.Subscription):
    class Arguments:
        pair = graphene.String(required=True)

    spread = graphene.Field(SpreadNode)

    @staticmethod
    def subscribe(root, info, pair, **kwargs):
        group_name = f'spread@{pair}'
        return [group_name]

    @staticmethod
    def publish(payload, info, **kwargs):
        return SpreadSubscription(spread=payload)
