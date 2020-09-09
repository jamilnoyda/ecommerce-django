from django.shortcuts import render


from rest_framework import viewsets
import json
from products.models import Product
from rest_framework import permissions


from django.core import serializers
from products.serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]

