from django.urls import path
from .views import manual_views

urlpatterns = [
    path('', manual_views.index, name="manual_index"),
]
