from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from datetime import datetime
from django.http import JsonResponse
class EventDetailAPI(APIView):
    def get(self, request, eventname):
        try:
            # Connect to MongoDB
            client = MongoClient('mongodb+srv://salmaa2:12345@cluster0.p3v58.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
            db = client['tazkarty']
            collection = db['events']
          

            # Log the eventname being fetched
            print(f"Fetching event with eventname: {eventname}")

            # Fetch the event
            event = collection.find_one({"eventname": eventname}, {'_id': 0})  # Exclude _id field
            if not event:
             return JsonResponse({"error": "Event not found"}, status=404)

            # Handle the date_time field
            if isinstance(event['date_time'], datetime):
                date_time = event['date_time'].strftime('%Y-%m-%d %H:%M:%S')
            else:
                timestamp = int(event['date_time']['$date']['$numberLong']) / 1000
                date_time = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

            # Handle the number_of_seats field
            if isinstance(event['number_of_seats'], dict):
                number_of_seats = int(event['number_of_seats']['$numberInt'])
            else:
                number_of_seats = event['number_of_seats']

            # Format the data
            event_data = {
                'eventname': event['eventname'],
                'organizer_name': event['organizer_name'],
                'title': event['title'],
                'description': event['description'],
                'date_time': date_time,
                'status': event['status'],
                'location': event['location'],
                'address': event['address'],
                'number_of_seats': number_of_seats,
                'eventPhoto': event['eventPhoto'],
          
            }

            return Response(event_data, status=status.HTTP_200_OK)

        except Exception as e:
            # Log the error
            print(f"Error: {str(e)}")
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
