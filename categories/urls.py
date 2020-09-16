from django.urls import include, path
from rest_framework import routers
from categories import views


from categories.views import (
    CategoryViewSet,
    CategoryCreate,
    CategoryDelete,
    CategoryUpdate,
    CategoryList,
    CategoryDetail,
)


router = routers.DefaultRouter()
router.register(r"categories-api", CategoryViewSet)

app_name = "categories"
urlpatterns = [
    path("", include(router.urls,)),
    path("category/add/", CategoryCreate.as_view(), name="category-add"),
    path("category/<int:pk>/", CategoryDetail.as_view(), name="category-detail"),
    path("category/<int:pk>/update/", CategoryUpdate.as_view(), name="category-update"),
    path("category/<int:pk>/delete/", CategoryDelete.as_view(), name="category-delete"),
    path("category/", CategoryList.as_view(), name="category-list"),
]
