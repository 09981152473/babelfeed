from django.urls import path
from .views.content_views import audio_view

urlpatterns = [
    path('audio/<str:show_id>/<uuid:audio_id>.mp3', audio_view, name="audio_file"),
]