from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from main.models import Data
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from django.urls import reverse
from main.forms import ProblemReport, CalorieTrackingForm
from main.models import Report, CalorieTracking


@csrf_exempt
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:data_information')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@csrf_exempt
def logout_user(request):
    logout(request)
    return redirect('main:data_list')

def data_list(request):
    data = Data.objects.all()
    return render(request, 'list.html', {'data': data})

@login_required(login_url="/login")
def data_information(request):
    data = Data.objects.all()
    return render(request, 'information.html', {'data': data})

def problem_report(request):
    form = ProblemReport(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:data_list'))

    context = {'form': form}
    return render(request, "problem_report.html", context)

def report_list(request):
    reports = Report.objects.all()

    context = {
        'reports': reports
    }

    return render(request, "report_list.html", context)

def calorie_tracking(request):
    # Get all items added to the user's tracking
    tracking_items = CalorieTracking.objects.filter(user=request.user)
    
    if request.method == 'POST':
        form = CalorieTrackingForm(request.POST)
        if form.is_valid():
            # Get the selected item from the form
            item_id = form.cleaned_data['item']
            item = Data.objects.get(pk=item_id)
            
            # Create a new CalorieTracking entry for the current user and selected item
            CalorieTracking.objects.create(user=request.user, item=item)
            
            # Redirect the user to the data information page
            return redirect('main:data_information')
    else:
        # If it's a GET request, display the form
        form = CalorieTrackingForm()
    
    return render(request, 'calorie_tracking.html', {'form': form, 'tracking_items': tracking_items})

def add_to_tracking(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        item = get_object_or_404(Data, pk=item_id)
        CalorieTracking.objects.create(user=request.user, item=item)
        # Redirect to the calorie tracking page
        return redirect('main:calorie_tracking')
    else:
        return HttpResponseNotAllowed(['POST'])