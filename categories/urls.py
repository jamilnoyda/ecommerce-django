from django.urls import include, path
from rest_framework import routers
from categories import views

router = routers.DefaultRouter()
router.register(r"categories", views.CategoryViewSet)

app_name = "categories"
urlpatterns = [
    
    path("", include(router.urls,)),
]
