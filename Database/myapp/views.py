# views.py
from django.shortcuts import render
from .models import Societe

def home_view(request):
    return render(request, 'myapp/home.html')

def societe_view(request):
    societes = Societe.objects.all()
    context = {
        'societes': societes
    }
    return render(request, 'myapp/societe.html', context)
