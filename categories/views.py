from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend


from rest_framework import viewsets
import json
from categories.models import Category
from rest_framework import permissions


from django.core import serializers
from categories.serializers import CategorySerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name']
    

