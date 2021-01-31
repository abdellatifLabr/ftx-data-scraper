import graphene
import channels_graphql_ws

from ..models import Pair
from .nodes import SpreadNode


class SpreadSubscription(channels_graphql_ws.Subscription):
    class Arguments:
        pair_id = graphene.ID(required=True)

    spread = graphene.Field(SpreadNode)

    @staticmethod
    def subscribe(root, info, pair_id, **kwargs):
        try:
            pair = Pair.objects.get(pk=pair_id)
        except Pair.DoesNotExist:
            raise Exception('This pair does not exist')

        group_name = f'spread@{pair.id}'
        return [group_name]

    @staticmethod
    def publish(payload, info, **kwargs):
        return SpreadSubscription(spread=payload)
