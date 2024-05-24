from django.urls import path
from . import views

urlpatterns = [
    path('', views.mood_list, name='mood_list'),
    path('create/', views.mood_create, name='mood_create'),
    path('links/<str:mood_name>/', views.mood_links, name='mood_links'),
]
