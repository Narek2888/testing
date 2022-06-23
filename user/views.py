from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from . forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(
                email = form.cleaned_data['email'],
                password1 = form.cleaned_data['password1']
            )
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    # if request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         user = form.get()
    #         user = authenticate(
    #             email = form.cleaned_data['email'],
    #             password1 = form.cleaned_data['password1']
    #         )
    #         login(request, user)
    #         return render(request, 'home')
    # else:
    return render(request, 'login.html')