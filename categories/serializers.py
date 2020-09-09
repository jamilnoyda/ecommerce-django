from django.contrib.auth.models import Group
from rest_framework import serializers

from django.contrib.auth.models import User


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

        fields = "__all__"

