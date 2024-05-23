from django.shortcuts import render
from main.models import Data, User
from django.shortcuts import redirect, get_object_or_404
from main.forms import DataForm

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

def edit_data(request, pk):
    data = get_object_or_404(Data, pk=pk)

    if request.method == 'POST':
        form = DataForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect('admin:content_management') 
    else:
        form = DataForm(instance=data)

    return render(request, 'edit_data.html', {'form': form})