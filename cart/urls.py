from django.urls import path
from .views import RandomAPIClass

urlpatterns = [
    path('cart', RandomAPIClass)
]
