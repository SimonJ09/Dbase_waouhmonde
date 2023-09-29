# views.py
from django.shortcuts import render
from .models import Personne
import pandas as pd
from django.http import HttpResponse
import csv


def personne_view(request):
    personnes = Personne.objects.all()
    context = {
        'personnes': personnes
    }
    return render(request, 'myapp_personnes/personne.html', context)


def export_personnes_to_excel(request):
    # Récupérez toutes les données de la société
    personnes =Personne.objects.all()
    # Créez un DataFrame pandas avec les données
    data = {
        'Nom': [personne.nom for personne in personnes],
        'Emails': [personne.email for personne in personnes],
        'Numéro 1': [personne.numero1 for personne in personnes],
    }
    df = pd.DataFrame(data)
    # Créez un objet HttpResponse avec l'Excel en tant que contenu
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="personnes.xlsx"'
    # Écrivez le DataFrame dans un fichier Excel
    df.to_excel(response, index=False, engine='openpyxl')
    return response

def export_personnes_to_csv(request):
    # Récupérez toutes les données de la société
    personnes = Personne.objects.all()
    # Créez une réponse HTTP avec un type de contenu CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="personnes.csv"'

    # Créez un objet CSV Writer
    csv_writer = csv.writer(response)

    # Écrivez les en-têtes de colonnes
    csv_writer.writerow([
        'Nom ',
        'Emails',
        'Numéro 1',
    ])

    # Écrivez les données de la société dans le fichier CSV
    for personne in personnes:
        csv_writer.writerow([
            personne.nom,
            personne.email,
            personne.numero1,
          
        ])

    return response


def update_database_from_csv(file_path):
    data = pd.read_csv(file_path)
    for index, row in data.iterrows():
        mon_objet = MonModele.objects.get(id=row['id']) 
        mon_objet.champ1 = row['champ1']  
        mon_objet.champ2 = row['champ2']
        mon_objet.save()


if __name__ == "__main__":
    update_database_from_csv("chemin_vers_votre_fichier.csv")

