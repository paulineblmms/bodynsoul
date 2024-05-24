from django.shortcuts import render
from main.models import Report

def report_list(request):
    reports = Report.objects.all()

    context = {
        'reports': reports
    }

    return render(request, "report_list.html", context)