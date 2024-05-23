from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from main.models import Data

@login_required(login_url="/login")
def data_information(request):
    data = Data.objects.all()
    return render(request, 'information.html', {'data': data})

def data_list(request):
    data = Data.objects.all()
    return render(request, 'list.html', {'data': data})