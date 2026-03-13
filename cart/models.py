from django.db import models
from product.models import Product
from datetime import datetime, timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    class Meta:
        db_table= "Cart"

    def __str__(self):
        return f"{self.user}'s cart"
    
class CartItem(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, related_name="product")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    item_expiration = models.DateTimeField()

    def save(self):
        self.item_expiration = self.created_on + timedelta(days=7)
        return super().save()
    
    def __str__(self):
        return f"{self.product.name}"
