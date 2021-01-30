import graphene

import futures.schema


class Query(
    futures.schema.Query,
    graphene.ObjectType
):
    pass


class Subscription(
    futures.schema.Subscription,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query, subscription=Subscription)
