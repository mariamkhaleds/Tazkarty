from django.db import models
from djongo.models import ObjectIdField, URLField



class Event(models.Model):
    _id = ObjectIdField(primary_key=True, editable=False)
    address = models.TextField()
    date_time = models.DateTimeField()
    description = models.TextField()
    eventname = models.TextField()
    eventPhoto = models.URLField()
    location = models.URLField()
    number_of_seats = models.IntegerField()
    organizer_name = models.TextField()
    status = models.TextField()
    title = models.TextField()




class Meta:
    db_table = 'events'



