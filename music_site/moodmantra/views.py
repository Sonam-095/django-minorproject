from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import signupform
from .forms import loginform

# signup
def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()  # Save to the database
            return redirect('login')  # Redirect to login or another page
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})

# login
def login(request):
    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            password = form.cleaned_data['Password']
            print(f"Email: {email}, Password: {password}")  # Debug message
            return redirect('homepage')  # Redirect to homepage on successful login
        else:
            print("Form is invalid.")  # Debug message
            print(form.errors)  # Debug message to print form errors
            messages.error(request, 'Please correct the errors below.')
    else:
        form = loginform()

    return render(request, 'login.html', {'login': form})

# other pages
def moodinput(request):
    return render(request,'moodinput.html')

def recommendation(request):
    return render(request,'recommendation.html')