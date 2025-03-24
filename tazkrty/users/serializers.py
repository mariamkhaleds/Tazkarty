# from django.forms import ValidationError
# from rest_framework import serializers
# from django.contrib.auth.models import User, AbstractUser
# from django.contrib.auth.password_validation import validate_password
# from django.db import models
# from .models import customusers



# class UserRegistrationSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True)

#     class Meta:
#         model = customusers
#         fields = ('username', 'email', 'password', 'password2','role')
#         extra_kwargs = {'password': {'write_only': True}}

#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError({"password": "Passwords must match."})
#         return data

#     def create(self, validated_data):
#         validated_data.pop('password2')
#         user = customusers.objects.create_user(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
# # from django.contrib.auth import authenticate
# # from django.contrib.auth import get_user_model
# # from rest_framework import serializers
# # from rest_framework_simplejwt.tokens import RefreshToken

# # User = get_user_model()

# # class UserLoginSerializer(serializers.Serializer):
# #     email = serializers.EmailField()
# #     password = serializers.CharField(write_only=True)

# #     def validate(self, data):
# #         email = data.get("email")
# #         password = data.get("password")

# #         try:
# #             user = User.objects.get(email=email)  # Get user by email
# #         except User.DoesNotExist:
# #             raise serializers.ValidationError("Invalid email or password.")

# #         if not user.check_password(password):  # Check password manually
# #             raise serializers.ValidationError("Invalid email or password.")

# #         refresh = RefreshToken.for_user(user)
# #         return {
# #             "email": user.email,
# #             "username": user.username,
# #             "token": str(refresh.access_token)
# #         }

# # from django.contrib.auth import get_user_model
# # from rest_framework import serializers
# # from rest_framework_simplejwt.tokens import RefreshToken

# # User = get_user_model()

# # class UserLoginSerializer(serializers.Serializer):
# #     email = serializers.EmailField()
# #     password = serializers.CharField(write_only=True)

# #     class Meta:
# #         model = User
# #         fields = ('email', 'password')

# #     def validate(self, data):
# #         email = data.get("email")
# #         password = data.get("password")

# #         try:
# #             user = User.objects.get(email=email)  # البحث عن المستخدم بالإيميل
# #         except User.DoesNotExist:
# #             raise serializers.ValidationError({"error": "Invalid email or password."})

# #         if not user.check_password(password):  # التحقق من كلمة المرور
# #             raise serializers.ValidationError({"error": "Invalid email or password."})

# #         refresh = RefreshToken.for_user(user)  # إنشاء التوكنات

# #         return {
# #             "email": user.email,
# #             "username": user.username,
# #             "role": user.role,  # إرجاع الدور (إذا كان لديك في `customusers`)
# #             "access_token": str(refresh.access_token),
# #             "refresh_token": str(refresh),
# #         }
# from rest_framework import serializers
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)

#     def validate(self, data):
#         username = data.get('username')
#         password = data.get('password')

#         if not username or not password:
#             raise serializers.ValidationError("Both username and password are required.")

#         user = authenticate(username=username, password=password)

#         if not user:
#             raise serializers.ValidationError("Invalid credentials. Please try again.")

#         data['user'] = user  # Add authenticated user to validated data
#         return data

from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .models import customusers


class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = customusers
        fields = ('username', 'email', 'password', 'password2', 'role')
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
    
from django.utils.timezone import now
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import customusers

class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        try:
            user = customusers.objects.get(email=email)  # الحصول على المستخدم بالبريد الإلكتروني
        except customusers.DoesNotExist:
            raise serializers.ValidationError("Invalid email or password.")

        if not user.check_password(password):  # التحقق من صحة كلمة المرور
            raise serializers.ValidationError("Invalid email or password.")

        # ✅ تحديث `last_login`
        user.last_login = now()
        user.save(update_fields=["last_login"])  # تحديث الحقل فقط بدون التأثير على باقي الحقول

        # إنشاء التوكنات
        refresh = RefreshToken.for_user(user)

        return {
            "email": user.email,
            "username": user.username,
            "role": user.role,  # إرجاع دور المستخدم
            "last_login": user.last_login,  # ✅ إرجاع آخر تسجيل دخول
            "access_token": str(refresh.access_token),
            "refresh_token": str(refresh),
        }
