# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient

from datetime import datetime

  
class EventDetailAPI(APIView):
    def get(self, request,eventname):
        # Connect to MongoDB
       client = MongoClient('mongodb+srv://salmaa2:12345@cluster0.p3v58.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
       db = client['tazkarty']  # Replace with your database name
       collection = db['events']
       prices=db['ticket_prices']  # Replace with your collection name


        # Fetch the document
       event = collection.find_one({"eventname": eventname})
       ticket_prices=prices.find_one({"eventname": eventname})

       if not event:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

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
            'prices':ticket_prices['price'],
            'category':ticket_prices['category']
        }

       return Response(event_data, status=status.HTTP_200_OK)