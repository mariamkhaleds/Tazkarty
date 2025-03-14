from django.http import JsonResponse
from django.conf import settings
from pymongo import MongoClient
import logging

logger = logging.getLogger(__name__)
def get_all_events(request):
    try:
    # Connect to MongoDB using the Django settings
    # client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    # db_name = settings.DATABASES['default']['NAME']    
    # db = client[db_name]  
    # events_collection = db['events']    
    # events = events_collection.find()
     client = MongoClient('mongodb+srv://salmaa2:12345@cluster0.p3v58.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
     db = client['tazkarty']
     collection = db['events']
     events = list(collection.find({}, {'_id': 0}))

     logger.info(f"Fetched events: {events}")

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
    except Exception as e:
         logger.error(f"Error fetching events: {e}")
         return JsonResponse({"error": str(e)}, status=500)

     
