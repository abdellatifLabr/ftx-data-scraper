import graphene


from .queries import (
    SpreadQuery,
    FutureQuery,
)
from .subscriptions import (
    SpreadSubscription,
)


class Query(
    SpreadQuery,
    FutureQuery,
    graphene.ObjectType
):
    pass


class Subscription(graphene.ObjectType):
    spread = SpreadSubscription.Field()
