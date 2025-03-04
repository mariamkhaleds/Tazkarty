# from django.db import models

# # Create your models here.
# from djongo import models
# # from tazkrty.settings import db


# class Event(models.Model):
#     _id = models.ObjectIdField()  # MongoDB ObjectId field
#     eventname = models.CharField(max_length=255)
#     organizer_name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date_time = models.DateTimeField()
#     status = models.CharField(max_length=50)
#     location = models.URLField()
#     address = models.CharField(max_length=255)
#     number_of_seats = models.IntegerField()

#     class Meta:
#         db_table = "events"  # Name of the collection in MongoDB



# # class Bookings(models.Model):
# #     eventname = models.CharField(max_length=255)
# #     useremail = models.EmailField()
# #     ticket_number = models.CharField(max_length=100)
# #     purchase_date = models.DateTimeField()
# #     status = models.CharField(max_length=50)

# #     class Meta:
# #         db_table = "bookings"  # This should match your MongoDB collection name

# #     def __str__(self):
# #         return f"{self.eventname} - {self.useremail}"



# class EventHistory:
#     """A class to represent event bookings in MongoDB."""

#     collection = db["bookings"]  # Replace with your collection name

#     @staticmethod
#     def get_history_by_email(email):
#         """Fetches booking history for a user by email."""
#         return list(EventHistory.collection.find({"useremail": email}))



from djongo import models
from django.conf import settings

# Ensure MongoDB connection
db = settings.DATABASES['default']['NAME']

class Event(models.Model):
    _id = models.ObjectIdField(primary_key=True)  
    eventname = models.CharField(max_length=255)
    organizer_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    location = models.URLField()
    address = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()

    class Meta:
        db_table = "events"  # MongoDB collection name


# class EventHistory:
#     """Class to fetch event booking history from MongoDB."""

#     @staticmethod
#     def get_history_by_email(email):
#         """Fetches event booking history for a given email."""
#         try:
#             # Initialize MongoDB client
#             client = MongoClient(settings.MONGODB_URI)  # Use Django settings for MongoDB URI
            
#             # Access the correct database
#             db = client[settings.MONGO_DB_NAME]  # Ensure you define this in settings.py
            
#             # Access the collection
#             collection = db["bookings"]  # Replace "bookings" with your actual collection name

#             # Fetch user history and exclude MongoDB "_id" field
#             user_events = list(collection.find({"useremail": email}, {"_id": 0}))

#             return user_events

#         except Exception as e:
#             print(f"Error fetching user history: {e}")  # Logging for debugging
#             return []  # Return an empty list if an error occurs

# class Booking(models.Model):
#     eventname = models.CharField(max_length=255)
#     useremail = models.EmailField()
#     ticket_number = models.CharField(max_length=50)
#     purchase_date = models.DateTimeField()
#     status = models.CharField(max_length=20)
    
#     def __str__(self):
#         return f"{self.eventname} - {self.useremail}"