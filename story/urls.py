from django.urls import path
from story import views
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('analyze_story/', views.analyze_story, name='analyze_story'),

]