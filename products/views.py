from django.shortcuts import render

import datetime
from rest_framework import viewsets
import json
from rest_framework.exceptions import NotFound
from products.models import Product
from rest_framework import permissions
from rest_framework.exceptions import APIException

from rest_framework.response import Response
from django.core import serializers
from products.serializers import ProductSerializer

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["name"]

    def create(self, request):
        today = datetime.date.today()

        todays_records = Product.objects.filter(created__gt=today)[:10]
        if todays_records.count() > 10:
            raise APIException("today limit reached")

        data = request.data.copy()

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:

            return Response(serializer.errors)

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        today = datetime.date.today()

        todays_records = Product.objects.filter(created__gt=today)[:10]
        if todays_records.count() > 10:
            raise APIException("today limit reached")

        serializer.save()
        return Response(serializer.data)

