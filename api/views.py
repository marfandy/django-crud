from api.serializer import ChildSerializer, GrandChildSerializer, ParentSerializer
from api import models
from rest_framework import serializers, status, generics
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema


class AuntView(generics.ListAPIView):
    serializer_class = ChildSerializer
    queryset = models.Child.objects.filter(
        fk_parent__name__icontains='budi', gender=models.Gender.Female)


class ChildView(generics.ListAPIView):
    serializer_class = ChildSerializer
    queryset = models.Child.objects.filter(fk_parent__name__icontains='budi')


class GrandChildView(generics.ListAPIView):
    serializer_class = GrandChildSerializer
    queryset = models.GrandChild.objects.filter(
        fk_child__fk_parent__name__icontains='budi')


class GrandChildFemaleView(generics.ListAPIView):
    serializer_class = GrandChildSerializer
    queryset = models.GrandChild.objects.filter(
        fk_child__fk_parent__name__icontains='budi', gender=models.Gender.Female)


class CousinView(generics.ListAPIView):
    serializer_class = GrandChildSerializer
    queryset = models.GrandChild.objects.filter(
        fk_child__fk_parent__name__icontains='budi', gender=models.Gender.Male)
