from django.urls import path
from main.views import register, login_user, logout_user, data_list, home, problem_report

app_name = 'main'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('list/', data_list, name='data_list'),
    path('', home, name='home'),
    path('problem-report', problem_report, name='problem_report'),


]
