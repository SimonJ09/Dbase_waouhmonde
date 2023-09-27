from django.shortcuts import render, redirect

def accueil(request):
    return render(request, 'Database/acceuil.html')