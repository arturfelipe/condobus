import graphene
from graphene_django.converter import convert_django_field
from graphene_django.types import DjangoObjectType

from django.contrib.gis.db import models
from transport.models import Bus, Direction, Route, StopPoint, TimeSheet, Travel


@convert_django_field.register(models.PointField)
def convert_PointField(field, registry=None):
    return graphene.String()


class TimeSheetType(DjangoObjectType):
    class Meta:
        model = TimeSheet


class TravelType(DjangoObjectType):
    class Meta:
        model = Travel


class RouteType(DjangoObjectType):
    class Meta:
        model = Route


class StopPointType(DjangoObjectType):
    class Meta:
        model = StopPoint


class DirectionType(DjangoObjectType):
    class Meta:
        model = Direction


class BusType(DjangoObjectType):
    class Meta:
        model = Bus


class Query(object):
    time_sheets = graphene.List(TimeSheetType)

    travels = graphene.List(TravelType)

    direction = graphene.Field(
        DirectionType,
        id=graphene.Int(),
        name=graphene.String()
    )

    route = graphene.Field(
        RouteType,
        id=graphene.Int(),
        name=graphene.String()
    )

    stop_point = graphene.Field(
        StopPointType,
        id=graphene.Int(),
        name=graphene.String()
    )

    bus = graphene.Field(
        BusType,
        id=graphene.Int(),
        name=graphene.String()
    )

    def resolve_time_sheets(self, info, **kwargs):
        return TimeSheet.objects.all()
