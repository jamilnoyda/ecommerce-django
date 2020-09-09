from django.contrib.auth.models import Group
from rest_framework import serializers

from categories.models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category

        fields = "__all__"

