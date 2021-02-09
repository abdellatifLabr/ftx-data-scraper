import channels_graphql_ws
import graphene

from ..models import Pair
from .nodes import SpreadNode


class SpreadSubscription(channels_graphql_ws.Subscription):
    class Arguments:
        pairs_ids = graphene.List(graphene.ID, required=True)

    spread = graphene.Field(SpreadNode)

    @staticmethod
    def subscribe(root, info, pairs_ids, **kwargs):
        groups = []
        for pair_id in pairs_ids:
            try:
                pair = Pair.objects.get(pk=pair_id)
            except Pair.DoesNotExist:
                continue

            groups.append(f'spreads@{pair.id}')

        return groups

    @staticmethod
    def publish(payload, info, **kwargs):
        return SpreadSubscription(spread=payload)
