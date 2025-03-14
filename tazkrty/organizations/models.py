from django.db import models

# Create your models here.
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
