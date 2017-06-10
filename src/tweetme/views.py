
from django.db.models import Q
from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, "home.html", {})

def love(request):
    return render(request, "love.html", {})
