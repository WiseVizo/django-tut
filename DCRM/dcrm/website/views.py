from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(req):
    return render(req, "home.html", {})