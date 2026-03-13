from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from django_redis import get_redis_connection
from .models import Product

@receiver([pre_save, post_delete], sender=Product)
def invalidate_cache(*args, **kwargs):
    redis_client = get_redis_connection("default")
    print(redis_client)
    print(redis_client.keys)
    delete_multiple_patterned_keys("product_list", redis_client)
    

def delete_multiple_patterned_keys(pattern: str, redis_client) -> None:
    keys = redis_client.keys(pattern)
    if keys:
        redis_client.delete(*keys)

    
