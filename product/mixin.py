from django.core.cache import cache
from rest_framework.response import Response
from rest_framework import status

#  Cache to store products info for one hr.
class CachedListMixin:
    cache_timeout = 60 * 60 * 1

    def list(self, request, *args, **kwargs):
        cache_key = "product_list"
        
        data = cache.get(cache_key)
        if data:
            print("cache hit 🔨✅")
            return Response(data, status=status.HTTP_200_OK)
        
        print("cache miss 🚀❌")
        response = super().list(request, *args, **kwargs)
        cache.set(cache_key, response.data, self.cache_timeout)
        return Response(response.data, status= status.HTTP_200_OK)