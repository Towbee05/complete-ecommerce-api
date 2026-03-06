from django.urls import path
from .views import UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = "authentication"
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="auth_signup"),
    path('login/', TokenObtainPairView.as_view(), name="auth_login"),
    path('login/refresh/', TokenRefreshView.as_view(), name="refresh_token")
]