from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.response import Response

from rest_framework import viewsets
import json
from categories.models import Category
from rest_framework import permissions

from rest_framework.exceptions import APIException

from django.core import serializers
from categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category.objects.all().order_by("-created")
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        today = datetime.date.today()

        todays_records = Category.objects.filter(updated_at__gt=today)[:10]
        if todays_records.count() > 10:
            raise APIException("today limit reached")

        serializer.save()
        return Response(serializer.data)


