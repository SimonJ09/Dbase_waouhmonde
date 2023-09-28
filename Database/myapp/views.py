# views.py
from django.shortcuts import render
from .models import Societe
import pandas as pd
from django.http import HttpResponse
from myapp.models import Societe
import csv

def home_view(request):
    return render(request, 'myapp/home.html')

def societe_view(request):
    societes = Societe.objects.all()
    context = {
        'societes': societes
    }
    return render(request, 'myapp/societe.html', context)

def update_database_from_csv(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        mon_objet = MonModele.objects.get(id=row['id']) 
        mon_objet.champ1 = row['champ1']  
        mon_objet.champ2 = row['champ2']
        mon_objet.save()


def export_societe_to_excel(request):
    # Récupérez toutes les données de la société
    societes = Societe.objects.all()
    # Créez un DataFrame pandas avec les données
    data = {
        'Nom de la société': [societe.nom for societe in societes],
        'Secteur': [societe.secteur for societe in societes],
        'Emails': [societe.emails for societe in societes],
        'Numéro 1': [societe.numero1 for societe in societes],
        'Numéro 2': [societe.numero2 for societe in societes],
        'Numéro 3': [societe.numero3 for societe in societes],
        'Téléphone fixe': [societe.fixe for societe in societes],
    }
    df = pd.DataFrame(data)
    # Créez un objet HttpResponse avec l'Excel en tant que contenu
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="societes.xlsx"'
    # Écrivez le DataFrame dans un fichier Excel
    df.to_excel(response, index=False, engine='openpyxl')
    return response

def export_societe_to_csv(request):
    # Récupérez toutes les données de la société
    societes = Societe.objects.all()

    # Créez une réponse HTTP avec un type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="societes.csv"'

    # Créez un objet CSV Writer
    csv_writer = csv.writer(response)

    # Écrivez les en-têtes de colonnes
    csv_writer.writerow([
        'Nom de la société',
        'Secteur',
        'Emails',
        'Numéro 1',
        'Numéro 2',
        'Numéro 3',
        'Téléphone fixe',
    ])

    # Écrivez les données de la société dans le fichier CSV
    for societe in societes:
        csv_writer.writerow([
            societe.nom,
            societe.secteur,
            societe.emails,
            societe.numero1,
            societe.numero2,
            societe.numero3,
            societe.fixe,
        ])

    return response



if __name__ == "__main__":
    update_database_from_csv("chemin_vers_votre_fichier.csv")

