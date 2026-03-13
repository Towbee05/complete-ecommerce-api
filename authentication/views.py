# TODO: 1. Add test for signup view to ensure it works as expected and handles edge cases properly ✅
# TODO: 2. Add rate limiting API for signup view to prevent abuse ✅
# TODO: 3. Add email verification to make sure new users are legitimate 
# TODO: 4. Ad4. Add google Sign-in
# TODO: 5. Ad4. Add github Sign-in

# !Did the following.
'''
1. Added an authentication endpoint
2. Addded a product catalog
3. Seeded categories into the database
4. Added cache to store products info for one hr.
'''

from django.shortcuts import render
from django.db import transaction
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from .serializers import UserSignupSerializer
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .throttling import AuthenticationBurstThrottle, AuthenticationSustainedThrottle
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import logging
import json

User = get_user_model()

# configure logging
logger = logging.getLogger(__name__)
# Create your views here.
class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer
    queryset = User.objects.all()
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AuthenticationBurstThrottle, AuthenticationSustainedThrottle]

    @transaction.atomic
    def create(self, request, *args, **kwargs) -> Response:
        try:
            logger.info('Signup process started')
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                logger.info("User successfully signed up!!!", extra={
                    "email": serializer.data.get('email')
                })
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            logger.warning("User signup attempt not successful", extra={
                "errors": serializer.errors,
                "payload": request.data
            })
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            logger.exception("Unexpected error during signup")
            return Response({"details": "Some server error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class UserLoginView(TokenObtainPairView):
    throttle_classes = [
        AuthenticationBurstThrottle,
        AuthenticationSustainedThrottle
        ]
