from django.shortcuts import render
from main.models import Data

def admin_landing(request):
    return render(request, 'admin_landing.html')

def content_management(request):
    data = Data.objects.all()
    context = {'data':data}
    return render(request, 'content_management.html', context)