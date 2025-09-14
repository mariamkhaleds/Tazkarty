from django.http import JsonResponse
from django.conf import settings
from pymongo import MongoClient
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import api_view


@swagger_auto_schema(
    operation_id='getAllEvents',
    operation_description='Retrieves a list of all events.',
    responses={
        200: openapi.Response(
            description='A list of events',
            schema=openapi.Schema(
                type=openapi.TYPE_ARRAY,
                items=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'title': openapi.Schema(type=openapi.TYPE_STRING, description='Title of the event'),
                        'description': openapi.Schema(type=openapi.TYPE_STRING, description='Description of the event'),
                        'date_time': openapi.Schema(type=openapi.TYPE_STRING, format=openapi.FORMAT_DATETIME, description='Date and time of the event'),
                        'location': openapi.Schema(type=openapi.TYPE_STRING, description='Location of the event'),
                        'eventPhoto': openapi.Schema(type=openapi.TYPE_STRING, description='URL or path to the event photo'),
                        'status': openapi.Schema(type=openapi.TYPE_STRING, description='Status of the event'),
                    },
                ),
            ),
        ),
        500: openapi.Response(description='Database connection error'),
    },
    method='get' 
)
@api_view(['GET']) 
def get_all_events(request):
    # Connect to MongoDB using the Django settings
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db_name = settings.DATABASES['default']['NAME']    
    db = client[db_name]  
    events_collection = db['events']    
    # events = events_collection.find()
    events = list(events_collection.find({}, {'_id': 0}))
    

    # data = [
    #     {
    #         "id": str(event["_id"]),
    #         "title": event.get("title", ""),
    #         "description": event.get("description", ""),
    #         "date_time": event.get("date_time", ""),
    #         "location": event.get("location", ""),
    #         "eventPhoto": event.get("eventPhoto", ""),
    #         "status": event.get("status", ""),
    #         "address": event.get("address", ""),
    #     }
    #     for event in events
    # ]
     # Ensure each event has the required fields
    formatted_events = []
    for event in events:
        formatted_event = {
            "title": event.get("title", "No Title"),
            "description": event.get("description", "No Description"),
            "date_time": event.get("date_time", "No Date"),
            "location": event.get("location", "No Location"),
            "eventPhoto": event.get("eventPhoto", ""),
            "status": event.get("status", "No Status"),
        }
        formatted_events.append(formatted_event)

    return JsonResponse(formatted_events, safe=False)


@api_view(['GET'])
def get_events_by_search(request):
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db_name = settings.DATABASES['default']['NAME']    
        db = client[db_name]  
        events_collection = db['events']
        events = list(events_collection.find({}, {'_id': 0}))
