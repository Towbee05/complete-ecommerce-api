from django.urls import path
from .views import UserSignupView

app_name = "authentication"
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="auth_signup")
]