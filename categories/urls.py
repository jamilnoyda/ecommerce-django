from django.urls import include, path
from rest_framework import routers
from products import views

router = routers.DefaultRouter()
router.register(r"product", views.ProductViewSet)

app_name = "products"
urlpatterns = [
    # path("api-token-auth/", views.obtain_auth_token),
    path("", include(router.urls,)),
]
