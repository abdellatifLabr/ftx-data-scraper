import graphene


class SpreadChartDataType(graphene.ObjectType):
    timestamp = graphene.DateTime()
    buy_spread = graphene.Float(required=True)
    sell_spread = graphene.Float(required=True)
