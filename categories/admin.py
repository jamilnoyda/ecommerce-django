from django.contrib import admin
from categories.models import Category

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    search_fields = ("name",)
    list_display = ("id", "name", "slug")

