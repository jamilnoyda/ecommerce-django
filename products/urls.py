from django.urls import include, path
from rest_framework import routers
from products import views
from products.views import (
    ProductViewSet,
    ProductCreate,
    ProductDelete,
    ProductUpdate,
    ProductList,
    ProductDetail,
)


router = routers.DefaultRouter()
router.register(r"product-api", ProductViewSet)

app_name = "products"

urlpatterns = [
    path("", include(router.urls,)),
    path("product/add/", ProductCreate.as_view(), name="product-add"),
    path("product/<int:pk>/", ProductDetail.as_view(), name="product-detail"),
    path("product/<int:pk>/update/", ProductUpdate.as_view(), name="product-update"),
    path("product/<int:pk>/delete/", ProductDelete.as_view(), name="product-delete"),
    path("product/", ProductList.as_view(), name="product-list"),
]
