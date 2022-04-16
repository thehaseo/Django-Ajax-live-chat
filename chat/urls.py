from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:room>/', views.room, name="room"),
    path('checkroom', views.check_room, name="check_room"),
    path('send', views.send_message, name='send_message'),
    path('getMessages/<str:room>/', views.get_messages, name='get_messages')
]