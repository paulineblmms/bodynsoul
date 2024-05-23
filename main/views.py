from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Data
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProblemReport
from main.models import Report

def report_list(request):
    reports = Report.objects.all()

    context = {
        'reports': reports
    }

    return render(request, "report_list.html", context)