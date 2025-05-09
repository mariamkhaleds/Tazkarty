from django.urls import include, path
from . import views 
from django.urls import path
from .views import UserLoginView
from .views import user_registration
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'users'

urlpatterns = [
    path('register/', user_registration, name='user_registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls')),
]    
