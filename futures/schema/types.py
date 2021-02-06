import graphene


class SpreadChartDataType(graphene.ObjectType):
    timestamp = graphene.DateTime()
    buy_spread = graphene.Float()
    sell_spread = graphene.Float()
