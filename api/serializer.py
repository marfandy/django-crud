from rest_framework import serializers
from api import models


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Parents
        fields = "__all__"


class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Child
        fields = "__all__"


class GrandChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GrandChild
        fields = "__all__"
