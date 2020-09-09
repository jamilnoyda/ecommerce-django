from django.contrib import admin

# Register your models here.


from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    search_fields = ("name",)

    list_display = (
        
        "category",
    )
    list_filter = (("category", admin.RelatedOnlyFieldListFilter),)

