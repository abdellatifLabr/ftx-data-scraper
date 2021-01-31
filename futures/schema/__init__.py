import graphene


from .queries import (
    SpreadQuery,
    FutureQuery,
    PairQuery,
    SpreadChartQuery,
)
from .subscriptions import (
    SpreadSubscription,
)


class Query(
    SpreadQuery,
    FutureQuery,
    PairQuery,
    SpreadChartQuery,
    graphene.ObjectType
):
    pass


class Subscription(graphene.ObjectType):
    spread = SpreadSubscription.Field()
