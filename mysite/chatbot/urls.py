from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.chatbot_api, name='chatbot_api'),
]
