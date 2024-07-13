from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.

def home_View(requests):
    return render(requests,'app/index.html')