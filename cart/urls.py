from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet, CartView

routers = DefaultRouter()
# routers.register(r'cart', CartView)
routers.register(r'cartitem', CartItemViewSet, basename="cartitems")

urlpatterns = [
    path("", CartView.as_view(), name="cart"),
    path("", include(routers.urls))
]
