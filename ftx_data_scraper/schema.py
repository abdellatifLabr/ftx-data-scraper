import graphene

import futures.schema


class Query(
    futures.schema.Query,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=Query)
