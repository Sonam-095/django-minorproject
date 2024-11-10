from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignupForm, LoginForm

# Signup view
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! You can now log in.')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# Login view
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('moodinput')  # Redirect on successful login
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# other pages
def moodinput(request):
    return render(request,'moodinput.html')

def recommendation(request):
    return render(request,'recommendation.html')