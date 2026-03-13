from django.db import models
import uuid
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'Category'
        indexes = [
            models.Index(fields=['name'])
        ]

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField()
    thumbnail = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="category")
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Product"
        verbose_name_plural = "Products"
        indexes = [
            models.Index(fields=['id', 'name'])
        ]
    
    def __str__(self):
        return self.name

    # def get_quantity_left(self, name):
    #     return Product.objects.filter(name=name).count() - CartItem.objects.product(name=name).count()