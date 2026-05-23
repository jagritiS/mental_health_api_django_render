from django.urls import path
from .views import chat, moods

urlpatterns = [
    path("chat/", chat),
    path("moods/", moods),
]