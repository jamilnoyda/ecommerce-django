from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from products.models import Product

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
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Product.objects.all().order_by("-created")
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
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        today = datetime.date.today()

        todays_records = Product.objects.filter(updated_at__gt=today)[:10]
        if todays_records.count() > 10:
            raise APIException("today limit reached")

        serializer.save()
        return Response(serializer.data)


class ProductCreate(CreateView):

    # class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    fields = ["name","price","quantity","category"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class ProductUpdate(UpdateView):
    model = Product
    # fields = ["name"]
    fields = ["name","price","quantity","category"]


class ProductDelete(DeleteView):
    model = Product
    success_url = reverse_lazy("products:product-list")


class ProductList(ListView):
    model = Product


class ProductDetail(DetailView):
    model = Product

    # def get_object(self):
    # obj = super().get_object()
    # Record the last accessed date
    # obj.last_accessed = timezone.now()
    # obj.save()
    # return obj

