import graphene
from graphene_django.types import DjangoObjectType
from org.models import Organization


class OrganizationType(DjangoObjectType):
    class Meta:
        model = Organization


class Query(object):
    organizations = graphene.List(OrganizationType)

    def resolve_organizations(self, info, **kwargs):
        return Organization.objects.all()


