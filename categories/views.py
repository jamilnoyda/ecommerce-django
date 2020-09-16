from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django.urls import reverse_lazy

from rest_framework.response import Response
import datetime
from rest_framework import viewsets
import json
from categories.models import Category
from rest_framework import permissions
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView

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
    filterset_fields = ["name"]

    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        today = datetime.date.today()

        todays_records = Category.objects.filter(updated_at__gt=today)[:10]
        if todays_records.count() > 10:
            raise APIException("today limit reached")

        serializer.save()
        return Response(serializer.data)





class CategoryCreate(CreateView):

    # class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ["name","parent"]

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CategoryUpdate(UpdateView):
    model = Category
    queryset = Category.objects.filter()

    # fields = ["name"]
    fields = ["name","parent"]


class CategoryDelete(DeleteView):
    model = Category
    queryset = Category.objects.filter()

    success_url = reverse_lazy("products:product-list")


class CategoryList(ListView):
    # import pdb; pdb.set_trace()
    model = Category
    queryset = Category.objects.filter()


class CategoryDetail(DetailView):
    model = Category

    # def get_object(self):
    # obj = super().get_object()
    # Record the last accessed date
    # obj.last_accessed = timezone.now()
    # obj.save()
    # return obj

