from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

