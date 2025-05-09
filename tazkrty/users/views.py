from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
####from .models import Event
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserRegistrationSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps
# from .models import EventHistory 
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        required=['username', 'email', 'password', 'password2'],
        properties={
            'username': openapi.Schema(type=openapi.TYPE_STRING, description='Desired username for the new user'),
            'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email address of the new user'),
            'password': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Password for the new user'),
            'password2': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_PASSWORD, description='Confirm password'),
            'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role of the new user (optional)'),
        },
    ),
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            description='User registered successfully',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Unique identifier of the new user'),
                    'username': openapi.Schema(type=openapi.TYPE_STRING, description='Username of the new user'),
                    'email': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_EMAIL, description='Email address of the new user'),
                    'role': openapi.Schema(type=openapi.TYPE_STRING, description='Role of the new user'),
                },
            ),
        ),
        status.HTTP_400_BAD_REQUEST: openapi.Response(
            description='Invalid input or registration failed',
            schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'username': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    'email': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    'password': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    'password2': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    'role': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING)),
                    'non_field_errors': openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(type=openapi.TYPE_STRING), description='Non-field specific errors (e.g., passwords mismatch)'),
                    
                },
            ),
        ),
    },
    operation_id='registerNewUser',
    operation_description='Registers a new user account, ensuring passwords match.',
)

@api_view(['POST'])
@parser_classes([JSONParser])
def user_registration(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=200)
        return Response(serializer.errors, status=400)

"""""

"""""