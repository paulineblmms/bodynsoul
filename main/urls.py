from django.urls import path
from main.views import register, login_user, logout_user, data_list, problem_report, report_list, data_information

app_name = 'main'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('', data_list, name='data_list'),
    path('problem-report', problem_report, name='problem_report'),
    path('report-list', report_list, name='report_list'),
    path('nutritional-information', data_information, name='data_information')
]
