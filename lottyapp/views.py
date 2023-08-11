from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LotteryEntryForm
from django.shortcuts import render
from .models import LotteryEntry
from django.contrib.auth.decorators import login_required
def index(request):
    participants = Participant.objects.all()
    return render(request, 'index.html', {'participants':participants})

def lottery_entry(request):
    if request.method == 'POST':
        form = LotteryEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Replace 'lottery_success' with the name of the success page URL
    else:
        form = LotteryEntryForm()
    return render(request, 'game.html', {'form': form})



from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after successful registration
    else:
        form = RegistrationForm()

    return render(request, 'signup.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationForm

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page or any other page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

from django.db.models import Count

def home(request):
    entries = LotteryEntry.objects.all()
    logged_in_username = request.user.username

    if logged_in_username == "alpha1":
        target_affiliation_code = "a1"
    elif logged_in_username == "alpha2":
        target_affiliation_code = "a2"
    elif logged_in_username == "alpha3":
        target_affiliation_code = "a3"
    # Add more cases for other salespersons as needed
    else:
        target_affiliation_code = None  # Default case if no match is found

    affiliation_counts = {}  # Dictionary to store counts for each affiliation

    if target_affiliation_code:
        filtered_entries = LotteryEntry.objects.filter(affiliation=target_affiliation_code)

        # Count entries for each affiliation
        affiliation_counts[target_affiliation_code] = filtered_entries.count()
    else:
        filtered_entries = []

    return render(request, 'dashboard.html', {'filtered_entries': filtered_entries, 'affiliation_counts': affiliation_counts})


def user_logout(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the URL name of your login page


from django.shortcuts import render
from .models import LotteryEntry  # Replace with your actual model import
from django.contrib.auth.decorators import login_required

@login_required
def filtered_lottery_entries(request):
    logged_in_username = request.user.username

    if logged_in_username == "alpha1":
        target_affiliation_code = "a1"
    elif logged_in_username == "alpha2":
        target_affiliation_code = "a2"
    elif logged_in_username == "alpha3":
        target_affiliation_code = "a3"
    # Add more cases for other salespersons as needed
    else:
        target_affiliation_code = None  # Default case if no match is found

    if target_affiliation_code:
        filtered_entries = LotteryEntry.objects.filter(affiliation_code=target_affiliation_code)
    else:
        filtered_entries = []

    return render(request, 'dashboard.html', {'filtered_entries': filtered_entries})


from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
from .models import Participant

def upload_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        data = pd.read_excel(excel_file)

        for index, row in data.iterrows():
            participant = Participant(
                name=row['name'],
                phonenumber=row['phonenumber'],
                winnings=row['winnings']
            )
            participant.save()

        return HttpResponse("Data uploaded successfully!")
    
    return render(request, 'upload_excel.html')
