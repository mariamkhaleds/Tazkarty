from django.http import JsonResponse
from django.conf import settings
from pymongo import MongoClient

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
            "address": event.get("address", "No Address"),
        }
        formatted_events.append(formatted_event)

    return JsonResponse(formatted_events, safe=False)
