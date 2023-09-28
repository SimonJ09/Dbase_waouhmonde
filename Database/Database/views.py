from django.shortcuts import render, redirect

def accueil(request):
    return render(request, 'Database/acceuil.html')

def homes(request):
    return render(request, 'Database/homes.html')