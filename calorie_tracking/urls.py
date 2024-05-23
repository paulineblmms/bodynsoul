from django.urls import path
from calorie_tracking.views import calorie_tracking, add_to_tracking, stats

app_name = "calorie_tracking"

urlpatterns = [
    path('calorie_tracking/', calorie_tracking, name='calorie_tracking'),
    path('add_to_tracking/', add_to_tracking, name='add_to_tracking'),
    path('stats/', stats, name='stats')
    ]