import graphene


from .queries import (
    SpreadQuery,
    FutureQuery,
)


class Query(
    SpreadQuery,
    FutureQuery,
    graphene.ObjectType
):
    pass
