import graphene


class SpreadChartDataType(graphene.ObjectType):
    minute = graphene.DateTime()
    hour = graphene.DateTime()
    day = graphene.DateTime()
    buy_spread = graphene.Float(required=True)
    sell_spread = graphene.Float(required=True)
