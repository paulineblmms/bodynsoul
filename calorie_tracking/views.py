from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from main.models import Data
from django.http import HttpResponseNotAllowed
from main.forms import CalorieTrackingForm
from main.models import CalorieTracking

def calorie_tracking(request):
    tracking_items = CalorieTracking.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = CalorieTrackingForm(request.POST)
        if form.is_valid():
            item_id = form.cleaned_data['item']
            item = Data.objects.get(pk=item_id)
            
            CalorieTracking.objects.create(user=request.user, item=item)
            
            return redirect('main:data_information')
    else:
        form = CalorieTrackingForm()
    
    return render(request, 'calorie_tracking.html', {'form': form, 'tracking_items': tracking_items})

def add_to_tracking(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Data, pk=item_id)
        CalorieTracking.objects.create(user=request.user, item=item)
        return redirect('main:calorie_tracking')
    else:
        return HttpResponseNotAllowed(['POST'])

def stats(request):
    return render(request, 'stats.html')
