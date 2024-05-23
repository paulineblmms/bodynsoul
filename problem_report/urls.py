from django.urls import path
from problem_report.views import problem_report

app_name = 'problem_report'

urlpatterns = [
    path('problem-report', problem_report, name='problem_report'),
]