# views.py
from django.shortcuts import render

def home(request):
    return render(request, 'HealthCareSystem/home.html')
