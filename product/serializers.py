from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_name(self, name: str) -> str:
        if not name.strip():
            raise serializers.ValidationError("Product name should not be empty")
        
        if Product.objects.filter(name__iexact=name).exists():
            raise serializers.ValidationError("A product with similar name exists in the DB.")
        return name
    
    def validate_description(self, desc: str) -> str:
        if not desc:
            raise serializers.ValidationError("Products should contain a description before creating.")
        return desc
        
    def validate_price(self, price: float) -> float:
        if price < 0:
            raise serializers.ValidationError("Entered price should be greater than zero.")
        return price

    def create(self, validated_data: dict) -> Product:
        product = Product.objects.create(**validated_data)
        product.save()
        return product