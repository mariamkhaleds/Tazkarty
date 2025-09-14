from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from users.models import customusers

class UserRegistrationTest(TestCase):
    databases = ['users_db']
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('users:user_registration')
        self.valid_payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Testpass123!',
            'password2': 'Testpass123!',
            'role': 'user'
        }
        self.invalid_payload = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'Testpass123!',
            'password2': 'Differentpass123!',
            'role': 'user'
        }
        self.missing_payload = {
            'email': 'test@example.com',
            'password': 'Testpass123!',
            'password2': 'Testpass123!',
            'role': 'user'
        }
        self.invalid_username_payload = {
            'username': 'test user',
            'email': 'test@example.com',
            'password': 'Testpass123!',
            'password2': 'Testpass123!',
            'role': 'user'
        }


    def test_user_registration_success(self):
        response = self.client.post(self.url, self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(customusers.objects.using('users_db').count(), 1)
        user = customusers.objects.using('users_db').get(username='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'user')
        self.assertTrue(user.check_password('Testpass123!'))

    def test_user_registration_password_mismatch(self):
        response = self.client.post(self.url, self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('password' , response.data )
        self.assertEqual(response.data['password'], ["Passwords must match."])
        self.assertEqual(customusers.objects.using('users_db').count(),0)

    def test_user_registration_missing_fields(self):
        response = self.client.post(self.url, self.missing_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(customusers.objects.using('users_db').count() , 0 )
    
    def test_invalid_username(self):
        response = self.client.post(self.url , self.invalid_username_payload , format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('username' , response.data)
        self.assertEqual(customusers.objects.using('users_db').count() , 0 )
    

        
 