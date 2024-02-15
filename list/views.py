from django.shortcuts import render
from .models import Data

def data_list(request):
    data = Data.objects.all()
    return render(request, 'list.html', {'data': data})
