from django.db import models

# Create your models here.
from djongo import models
from django.conf import settings

# Ensure MongoDB connection
db = settings.DATABASES['default']['NAME']

# class Event(models.Model):
#     _id = models.ObjectIdField(primary_key=True)  
#     eventname = models.CharField(max_length=255)
#     organizer_name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     date_time = models.DateTimeField()
#     status = models.CharField(max_length=50)
#     location = models.URLField()
#     address = models.CharField(max_length=255)
#     number_of_seats = models.IntegerField()
#     eventPhoto = models.URLField(null=True, blank=True)
  


#     class Meta:
#         db_table = "events"  # MongoDB collection name


# from djongo import models

from djongo import models

class TicketCategory(models.Model):
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    seatsAvailable = models.IntegerField()
    seatsSold = models.IntegerField()

    class Meta:
        abstract = True  # ✅ Must be abstract for embedded documents

class Event(models.Model):
    _id = models.ObjectIdField(primary_key=True)  # ✅ Use ObjectId for Event
    eventname = models.CharField(max_length=255)
    organizer_name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time = models.DateTimeField()
    status = models.CharField(max_length=50)
    location = models.URLField()
    address = models.CharField(max_length=255)
    number_of_seats = models.IntegerField()
    eventPhoto = models.URLField()
    ticketCategories = models.ArrayField(model_container=TicketCategory)  # ✅ Embedded list

    class Meta:
        db_table = "events"
