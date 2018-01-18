import graphene

import org.schema


class Query(org.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
