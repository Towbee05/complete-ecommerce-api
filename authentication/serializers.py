from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class UserSignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        # Authenticate and validate user
        user = authenticate(email=email, password=password)
        
        # throw error if user does not exist
        if user is None:
            raise serializers.ValidationError("Provided credential is invalid")
        data["user"] = user
        return user