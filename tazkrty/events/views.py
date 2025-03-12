from django.http import JsonResponse
from django.conf import settings
from pymongo import MongoClient

def get_all_events(request):
    # Connect to MongoDB using the Django settings
    client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
    db_name = settings.DATABASES['default']['NAME']    
    db = client[db_name]  
    events_collection = db['events']    
    events = events_collection.find()

    data = [
        {
            "id": str(event["_id"]),
            "title": event.get("title", ""),
            "description": event.get("description", ""),
            "date_time": event.get("date_time", ""),
            "location": event.get("location", ""),
            "eventPhoto": event.get("eventPhoto", ""),
            "status": event.get("status", ""),
        }
        for event in events
    ]

    return JsonResponse(data, safe=False)