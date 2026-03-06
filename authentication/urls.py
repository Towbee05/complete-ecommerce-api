from django.urls import path
from .views import UserSignupView, UserLoginView

app_name = "authentication"
urlpatterns = [
    path('signup/', UserSignupView.as_view(), name="auth_signup"),
    path('login/', UserLoginView.as_view(), name="auth_login")
]