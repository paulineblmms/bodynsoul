from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from main.forms import ProblemReport

def problem_report(request):
    form = ProblemReport(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:data_list'))

    context = {'form': form}
    return render(request, "problem_report.html", context)
