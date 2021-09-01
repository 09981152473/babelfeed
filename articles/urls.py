from django.urls import path
from .views.article_view import index

urlpatterns = [
    path('', index, name="articles"),
    
    ]