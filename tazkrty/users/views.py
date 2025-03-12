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


@api_view(['POST'])
@parser_classes([JSONParser])
def user_registration(request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['POST'])
def login_view(request):
    username = request.data.get("username")
    password = request.data.get("password")
    
    user = authenticate(username=username, password=password)
    
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)


"""""

def insert_event(request):
    if request.method == "POST":
        eventname = request.POST.get("eventname")
        organizer_name = request.POST.get("organizer_name")
        title = request.POST.get("title")
        description = request.POST.get("description")
        date_time = request.POST.get("date_time")
        status = request.POST.get("status")
        location = request.POST.get("location")
        address = request.POST.get("address")
        number_of_seats = request.POST.get("number_of_seats")

        # Convert date_time string to datetime object
        date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")

        # Save to database
        event = Event(
            eventname=eventname,
            organizer_name=organizer_name,
            title=title,
            description=description,
            date_time=date_time,
            status=status,
            location=location,
            address=address,
            number_of_seats=int(number_of_seats)
        )
        event.save()

        return render(request, "users/Add_Event.html", {"message": "Event inserted successfully!"})

    return render(request, "users/Add_Event.html")

"""
# def get_booking_history(request):
#     email = request.GET.get("email")

#     # If no email is provided, return all bookings
#     if not email:
#         bookings = Bookings.objects.all().values()
#         return JsonResponse({"bookings": list(bookings)}, safe=False, status=200)

#     bookings = Bookings.objects.filter(useremail=email).values()

#     if not bookings:
#         return JsonResponse({"message": "No bookings found for this email"}, status=404)

#     return JsonResponse({"bookings": list(bookings)}, safe=False, status=200)

# @csrf_exempt
# def get_user_history(request, email='john.doe@example.com'):
#     """Fetches event booking history for a user by email."""
#     user_events = list(collection.find({"useremail": email}, {"_id": 0}))  # Exclude _id field

#     if not user_events:
#         return JsonResponse({"message": "No booking history found."}, status=404)

#     return JsonResponse({"history": user_events}, safe=False)

# def history_page(request):
#     """Render the HTML template for booking history lookup."""
#     return render(request, "users/history.html")

"""""
from django.shortcuts import render
from pymongo import MongoClient
from django.conf import settings
client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
db = client["tazkarty"]  # Your database name
collection = db["bookings"]  # Your collection name

def booking_history(request, email):
    # Fetch all bookings for a specific email
    bookings = list(collection.find({"useremail": email}, {"_id": 0}))  # Exclude _id

    return render(request, 'users/history.html', {'bookings': bookings})

"""""