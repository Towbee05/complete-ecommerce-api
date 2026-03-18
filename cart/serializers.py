from rest_framework import serializers
from .models import Cart, CartItem
from product.models import Product

class CartItemSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(default= 1)
    cart = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CartItem
        fields = ['product', 'cart', 'quantity', 'created_on', 'item_expiration']

    def validate_quantity(self, quantity):
        if quantity < 1:
            raise serializers.ValidationError("Quantity of product should be greater than 1")
        return quantity
    
    def create(self, validated_data: dict):
        product_id = validated_data.get("product")
        quantity = validated_data.get("quantity")
        request = self.context.get("request")
        user = request.user
        
        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product_id, defaults={"quantity": quantity})
        if not item_created:
            cart_item.quantity += quantity
            cart_item.save()
            
        return cart_item

class CartSerializer(serializers.ModelSerializer):
    cart_items = CartItemSerializer(many=True, read_only=True)
    class Meta:
        model = Cart
        fields = ['id', 'cart_items']

    