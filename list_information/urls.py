from django.urls import path
from list_information.views import data_information, data_list

app_name = "list_information"

urlpatterns = [
    path('nutritional-information', data_information, name='data_information'),
    path('', data_list, name='data_list')
]