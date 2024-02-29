from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in successfully')
             # Clear all previous messages
            storage = messages.get_messages(request)
            storage.used = True
            return redirect('home')  # Redirect to a home page
        else:
            messages.error(request, 'Invalid username or password.')
             # Clear all previous messages
            storage = messages.get_messages(request)
            storage.used = True
    return render(request, "home.html", {})

# def login_user(req):
#      return render(req, "home.html", {})

def logout_user(request):
    logout(request)
    messages.success(request,"you have logged out!")
    return redirect("home")

def register_user(request):
    return render(request, "register.html", {})