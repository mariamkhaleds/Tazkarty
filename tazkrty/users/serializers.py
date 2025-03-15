from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.password_validation import validate_password
from django.db import models
from .models import customusers



class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = customusers
        fields = ('username', 'email', 'password', 'password2','role')
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords must match."})
        return data

    def create(self, validated_data):
        validated_data.pop('password2')
        user = customusers.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = User.objects.get(email=email)  # Get user by email
        except User.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.check_password(password):  # Check password manually
            raise serializers.ValidationError("Invalid email or password.")

        refresh = RefreshToken.for_user(user)
        return {
            "email": user.email,
            "username": user.username,
            "token": str(refresh.access_token)
        }
