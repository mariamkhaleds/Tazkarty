from rest_framework import serializers
from .models import Event, TicketCategory
from bson import ObjectId

class ObjectIdField(serializers.Field):
    """ Serializer field to handle MongoDB ObjectIds correctly """
    def to_representation(self, value):
        return str(value)  # Convert ObjectId to string for JSON

    def to_internal_value(self, data):
        return ObjectId(data)  # Convert string back to ObjectId

class TicketCategorySerializer(serializers.Serializer):  
    category = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    seatsAvailable = serializers.IntegerField()
    seatsSold = serializers.IntegerField()

class EventSerializer(serializers.ModelSerializer):
    _id = ObjectIdField(read_only=True)  # ✅ Handle ObjectId correctly
    ticketCategories = TicketCategorySerializer(many=True)  

    class Meta:
        model = Event
        fields = '__all__'

    def create(self, validated_data):
        ticket_data = validated_data.pop('ticketCategories', [])  # ✅ Extract tickets
        event = Event.objects.create(**validated_data)
        event.ticketCategories = ticket_data  # ✅ Embed tickets inside Event
        event.save()
        return event
