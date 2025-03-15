from django.urls import include, path
from . import views 
from django.urls import path
from .views import UserLoginView
from rest_framework_simplejwt.views import TokenRefreshView
app_name = 'users'

urlpatterns = [
    path('register/', views.user_registration, name='register'),
    #path('login/', views.login_view, name='login'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), 
name='token_refresh'),
    #######path('insert_event/', views.insert_event, name="insert_event"),
    path('api-auth/', include('rest_framework.urls')),
      #path('history/<str:email>/', views.get_user_history, name="history"),
    # path('history/', views.history_page, name="history_page"),
    #####path('history/<str:email>/', views.booking_history, name='booking_history'),
]    
