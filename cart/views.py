# TODO: 1. create a test function to make sure cart.get_total_cartitems is correct
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import CartItemSerializer, CartSerializer
from .models import CartItem, Cart
import logging 
# Create your views here.

logger = logging.getLogger(__name__)
class CartView(RetrieveAPIView):
    # queryset = Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        cart, _ = Cart.objects.get_or_create(user=self.request.user)

        logger.info(cart.get_total_cartitems())
        for item in cart.cart_items.all():
            logger.info(f"Price {item.product.name} ==> {item.product.price}")
            logger.info(f"Quantity {item.product.name} ==> {item.quantity}")
            logger.info(f"Total {item.product.name} ==> {item.quantity * item.product.price}")
            print(f"Product {item.product.name} ==> {item.product.quantity}")
        logger.info(cart.get_total_cartitems)
        print(cart.get_total_cartitems)
        return cart

class CartItemViewSet(ModelViewSet):
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return CartItem.objects.filter(cart=self.request.user.cart)