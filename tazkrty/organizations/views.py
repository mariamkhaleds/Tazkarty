from django.shortcuts import render
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Event
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
# from .serializers import UserRegistrationSerializer
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
# from .serializers import UserRegistrationSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from bson.json_util import dumps





# Create your views here.

# def insert_event(request):
#     if request.method == "POST":
#         eventname = request.POST.get("eventname")
#         organizer_name = request.POST.get("organizer_name")
#         title = request.POST.get("title")
#         description = request.POST.get("description")
#         date_time = request.POST.get("date_time")
#         status = request.POST.get("status")
#         location = request.POST.get("location")
#         address = request.POST.get("address")
#         number_of_seats = request.POST.get("number_of_seats")
#         eventPhoto = request.POST.get("eventPhoto")

#         # Convert date_time string to datetime object
#         date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")

#         # Save to database
#         event = Event(
#             eventname=eventname,
#             organizer_name=organizer_name,
#             title=title,
#             description=description,
#             date_time=date_time,
#             status=status,
#             location=location,
#             address=address,
#             number_of_seats=int(number_of_seats),
#             eventPhoto=eventPhoto
#         )
#         event.save()

#         return render(request, "organizations/Add_Event.html", {"message": "Event inserted successfully!"})

#     return render(request, "organizations/Add_Event.html")


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Event
from .serializers import EventSerializer

# @api_view(['POST'])
# def insert_event(request):
#     serializer = EventSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def get_events(request):
#     events = Event.objects.all().values()
#     return JsonResponse(list(events), safe=False)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny

class InsertEventView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# from django.http import JsonResponse
# from datetime import datetime
# from .models import Event
# from bson import ObjectId  # استيراد ObjectId من bson
# from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
# def insert_event(request):
#     if request.method == "POST":
#         try:
#             eventname = request.POST.get("eventname")
#             organizer_name = request.POST.get("organizer_name")
#             title = request.POST.get("title")
#             description = request.POST.get("description")
#             date_time = request.POST.get("date_time")
#             status = request.POST.get("status")
#             location = request.POST.get("location")
#             address = request.POST.get("address")
#             number_of_seats = request.POST.get("number_of_seats")
#             eventPhoto = request.POST.get("eventPhoto")

#             date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M")

#             event = Event(
#                 eventname=eventname,
#                 organizer_name=organizer_name,
#                 title=title,
#                 description=description,
#                 date_time=date_time,
#                 status=status,
#                 location=location,
#                 address=address,
#                 number_of_seats=int(number_of_seats),
#                 eventPhoto=eventPhoto
#             )
#             event.save()

#             # ✅ تحويل _id إلى string قبل إرساله في JSON
#             return JsonResponse({
#                 "message": "Event inserted successfully!",
#                 "event_id": str(event._id)  # تحويل ObjectId إلى string
#             })

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request method"}, status=400)



from django.shortcuts import render
from pymongo import MongoClient     
from django.conf import settings



try:
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
except KeyError:
    # Fallback or error handling
    print("MongoDB client settings not found, using default connection")
    client = MongoClient("localhost", 27017)
#db_name = settings.DATABASES['default']['NAME']  
db_name = 'tazkarty'  
db = client[db_name]  # Your database name
collection = db["bookings"]  # Your collection name

def booking_history(request, email):
    # Fetch all bookings for a specific email
    bookings = list(collection.find({"useremail": email}, {"_id": 0}))  # Exclude _id

    return JsonResponse({"history": bookings}, safe=False)

# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
# from django.conf import settings
# from pymongo import MongoClient
# from django.http import JsonResponse
# from datetime import datetime

# # Connect to MongoDB
# try:
#     client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
# except KeyError:
#     client = MongoClient("localhost", 27017)  # Fallback to localhost

# db = client['tazkarty']  # Database name
# collection = db['bookings']  # Collection name

# @login_required(login_url='/users/login/')
# def booking_history(request):
#     """ Fetch booking history for the logged-in user """
    
#     user = request.user  # Get the logged-in user
#     print("User:", user)  # Debugging
#     print("Is Superuser:", user.is_superuser)  # Debugging
#     print("User Email:", user.email)  # Debugging

#     if user.is_superuser:
#         # إذا كان المستخدم Superuser، اجلب جميع الحجوزات
#         bookings = list(collection.find({}, {"_id": 0}))
#     else:
#         # إذا كان المستخدم عاديًا، اجلب الحجوزات الخاصة ببريده الإلكتروني فقط
#         bookings = list(collection.find({"useremail": user.email}, {"_id": 0}))

#     # تحويل التواريخ إلى تنسيق مقروء
#     for booking in bookings:
#         if 'purchase_date' in booking:
#             if isinstance(booking['purchase_date'], dict) and '$date' in booking['purchase_date']:
#                 timestamp = int(booking['purchase_date']['$date']['$numberLong']) / 1000
#                 booking['purchase_date'] = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
#             elif isinstance(booking['purchase_date'], datetime):
#                 booking['purchase_date'] = booking['purchase_date'].strftime('%Y-%m-%d %H:%M:%S')

#     return render(request, 'organizations/history.html', {'bookings': bookings})
