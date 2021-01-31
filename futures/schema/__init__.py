import graphene


from .queries import (
    SpreadQuery,
    FutureQuery,
    PairQuery,
)
from .subscriptions import (
    SpreadSubscription,
)


class Query(
    SpreadQuery,
    FutureQuery,
    PairQuery,
    graphene.ObjectType
):
    pass


class Subscription(graphene.ObjectType):
    spread = SpreadSubscription.Field()
