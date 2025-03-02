from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('insert_event/', views.insert_event, name="insert_event"),
    
]