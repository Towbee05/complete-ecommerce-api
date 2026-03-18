from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet

routers = routers.DefaultRouter()
routers.register(r"", ProductViewSet)

app_name = "product"
urlpatterns = [
    path('', include(routers.urls))
]
