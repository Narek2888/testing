from distutils.log import error
from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, LogInForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):

    error = ""

    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
        error = form.errors
    context = {'form': form, 'error': error}
    return render(request, 'signup.html', context)

def login(request):
    if request.method == "POST":
        log_form = LogInForm(data=request.POST)
        if log_form.is_valid():
            return redirect('home')
    else:
        log_form = LogInForm()
    return render(request, 'login.html', {'log_form': log_form})