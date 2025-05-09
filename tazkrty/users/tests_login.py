# from django.test import TestCase
# from django.contrib.auth import get_user_model
# from .serializers import UserLoginSerializer  # تأكد أن المسار صحيح حسب مشروعك

# # استدعاء نموذج المستخدم المخصص
# customusers = get_user_model()

# class UserLoginSerializerTest(TestCase):
#     databases = {'users_db'}  # تحديد قاعدة البيانات المستخدمة

#     def setUp(self):
#         # إنشاء مستخدم تجريبي
#         self.user = customusers.objects.using('users_db').create_user(
#             username='testuser11',
#             email='test@example.com',
#             password='password@123'
#         )

#     def test_valid_user_login(self):
#         user_data = {
#             'username': 'testuser11',
#             'email': 'test@example.com',
#             'password': 'password@123',
#         }
#         serializer = UserLoginSerializer(data=user_data)
#         self.assertTrue(serializer.is_valid(), serializer.errors)

#     def test_invalid_user_login(self):
#         user_data = {
#             'username': 'testuser11',
#             'email': 'test@example.com',
#             'password': 'wrongpassword',
#         }
#         serializer = UserLoginSerializer(data=user_data)
#         self.assertFalse(serializer.is_valid())
