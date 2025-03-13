from djongo import models



# Define Location model
class Location(models.Model):
    name = models.CharField(max_length=100)
    map_link = models.URLField()  # Assuming the location has a map link

    class Meta:
        abstract = True  # Mark this model as abstract

    def __str__(self):
        return self.name

class Organizer(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

# Define Ticket model
class Ticket(models.Model):
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Example price field

    def __str__(self):
        return f'{self.category} - {self.price}'

# Define Event model
class Event(models.Model):
    image = models.URLField()
    time = models.DateTimeField()
    organizers = models.ArrayReferenceField(to=Organizer, on_delete=models.CASCADE)  # Many-to-Many relationship
    location = models.EmbeddedField(model_container=Location)  # Embedded document
    tickets = models.ArrayReferenceField(to=Ticket, on_delete=models.CASCADE)  # Many-to-Many relationship

    def __str__(self):
        return f'Event at {self.location.name} on {self.time}'