from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
#from django.shortcuts import render
from .models import Event
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps
# from .models import EventHistory 

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = UserCreationForm()
    return render(request, "users/register.html",{"form":
                                                  form})
    




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

