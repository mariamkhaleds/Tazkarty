#python manage.py test organizations.tests_history --keepdb
from django.test import TransactionTestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Event
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Event
from .serializers import EventSerializer
from rest_framework.permissions import AllowAny
from django.test import TestCase
from rest_framework.test import APIClient
from pymongo import MongoClient
from django.conf import settings

class BookingHistoryTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = '/organizations/history/hana@gmail.com'
        self.test_email = "hana@gmail.com"  # The email for the test

        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['CLIENT']['host'])
        db = client["tazkarty"]
        self.collection = db["bookings"]

        # Ensure there's a booking for the test email
        existing = self.collection.find_one({"useremail": self.test_email})
        self.assertIsNotNone(existing, f"No booking found for the email {self.test_email} in the database")

        # Optional: Add mock data here if needed to ensure clean test data

    def test_booking_history_view(self):
        response = self.client.get(f'/organizations/history/{self.test_email}/')
        
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertIn("history", data, "Response should contain 'history' key.")
        self.assertTrue(len(data["history"]) > 0, "Booking history should not be empty.")

        for booking in data["history"]:
            self.assertEqual(booking["useremail"], self.test_email, "Booking belongs to wrong email.")
            self.assertNotIn("_id", booking, "Response should not contain internal MongoDB '_id'.")
