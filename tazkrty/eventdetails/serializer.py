from rest_framework import serializers

class EventSerializer(serializers.Serializer):
    eventname = serializers.CharField()
    organizer_name = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    date_time = serializers.CharField()
    status = serializers.CharField()
    location = serializers.CharField()
    address = serializers.CharField()
    number_of_seats = serializers.IntegerField()
    eventPhoto = serializers.CharField()