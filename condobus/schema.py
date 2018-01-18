import graphene

import org.schema
import transport.schema


class Query(org.schema.Query, transport.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
