from django.shortcuts import render
from main.models import Data, User

def admin_landing(request):
    return render(request, 'admin_landing.html')

def content_management(request):
    data = Data.objects.all()
    context = {'data':data}
    return render(request, 'content_management.html', context)

def user_management(request):
    users = User.objects.all().exclude(is_superuser=True)
    context = {'users':users}
    return render(request, 'user_management.html', context)