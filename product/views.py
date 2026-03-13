# TODO 6. Add cache to store all products for 1 hour, and invalidate the cache when a product is created, updated, or deleted. ✅
# TODO 7. Add test for login endpoint, and products. ✅


from django.shortcuts import render
from .serializers import ProductSerializer
from .models import Product
from .mixin import CachedListMixin
from cart.models import Cart
from cart.models import CartItem
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.decorators import action
from django_redis import get_redis_connection


class ProductViewSet(CachedListMixin, ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [JWTAuthentication]