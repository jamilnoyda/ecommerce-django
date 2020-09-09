from django.db import models
from categories.models import Category
from django.urls import reverse

# Create your models here.


class Product(models.Model):
    class Meta:
        ordering = ("name",)
        verbose_name = "Product"
        verbose_name_plural = "Products"

    category = models.ForeignKey(
        Category, related_name="products", on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    # return reverse("shop:product_detail", args=[self.id, self.slug])

