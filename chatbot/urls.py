from django.urls import path
from . import views

urlpatterns = [
    path('', views.analyze_story, name='analyze_story'),  # Default route
]
