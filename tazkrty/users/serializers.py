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
    

