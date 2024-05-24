from django.urls import path
from mood_tracking.views import mood_tracking

app_name = 'main'

urlpatterns = [
    path('mood-tracking/', mood_tracking, name='mood_tracking'),
]
