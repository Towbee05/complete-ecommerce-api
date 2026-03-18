from django.db import models
from product.models import Product
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model

User = get_user_model()

def default_expiration():
    return timezone.now() + timedelta(days=7)

# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cart")
    class Meta:
        db_table= "Cart"

    def __str__(self):
        return f"{self.user}'s cart"

    def get_total_cartitems(self):
        total_sum = 0
        cartitems = self.cart_items.all()
        for item in cartitems:
            total_sum += ((item.quantity) * (item.product.price))
        return total_sum

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="cart_items")
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="cart_items")
    quantity = models.PositiveIntegerField(default=1)
    created_on = models.DateTimeField(auto_now_add=True)
    item_expiration = models.DateTimeField(blank=True, null=True, default= default_expiration)
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ["cart", "product"],
                name="unique_cart_product"
            )
        ]

    def __str__(self):
        return f"{self.product.name}"
