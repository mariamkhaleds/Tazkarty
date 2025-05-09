# python manage.py test organizations.tests --keepdb
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

class InsertEventViewTransactionTests(TransactionTestCase):
    """
    TransactionTestCase لا يقوم بفلش الـ DB بين كل اختبار
    وبالتالي يمكن تفقد السجلات بعد انتهاء الاختبار
    """
    reset_sequences = True
    serialized_rollback = True

    def setUp(self):
        self.client = APIClient()
        self.url = '/organizations/insert_event/'  # عدّل حسب URL الفعلي

        self.valid_payload = {
            "eventname": "Tech Conference",
            "organizer_name": "Tech Org",
            "title": "Annual Tech Meetup",
            "description": "A tech meetup for developers and tech enthusiasts.",
            "date_time": "2025-08-15T14:00:00Z",
            "status": "active",
            "location": "https://maps.example.com/location",
            "address": "123 Tech Street",
            "number_of_seats": 200,
            "eventPhoto": "https://example.com/photo.jpg",
            "ticketCategories": [
                {"category": "VIP", "price": 150, "seatsAvailable": 100, "seatsSold": 20},
                {"category": "Regular", "price": 100, "seatsAvailable": 100, "seatsSold": 50}
            ]
        }

        self.invalid_payload = {
            "organizer_name": "Tech Org",  # بيانات ناقصة عمدًا
            "ticketCategories": []
        }

    def test_create_event_success(self):
        """يتحقق من إنشاء الحدث بنجاح ويتركه في الـ DB بعد انتهاء الاختبار"""
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # نتأكد من وجود سجل واحد باستخدام values_list (تجنب AbstractField)
        count = Event.objects.count()
        self.assertEqual(count, 1)

        # استعلام الحقول الضرورية دون تحميل الـ ArrayField
        data = Event.objects.values('eventname', 'organizer_name', 'number_of_seats')[0]
        self.assertEqual(data['eventname'], "Tech Conference")
        self.assertEqual(data['organizer_name'], "Tech Org")
        self.assertEqual(data['number_of_seats'], 200)

    def test_create_event_failure(self):
        """يتحقق من رفض البيانات الناقصة"""
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('eventname', response.data)

