from django.urls import path
from . import views 

app_name = 'users'

urlpatterns = [
    path('register/', views.register_view, name="register"),
    path('insert_event/', views.insert_event, name="insert_event"),
    #path('history/<str:email>/', views.get_user_history, name="history"),
    # path('history/', views.history_page, name="history_page"),
    path('history/<str:email>/', views.booking_history, name='booking_history'),
]