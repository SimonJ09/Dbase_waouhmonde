# views.py
from django.shortcuts import render
from .models import Personne
import pandas as pd
from django.http import HttpResponse
import csv
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UploadFileForm
from .forms import RecherchePersonneForm

def recherche_personne(request):
    if request.method == 'POST':
        print('ok')
        form = RecherchePersonneForm(request.POST)
        print(('ok'))
        if form.is_valid():
            terme_recherche = form.cleaned_data['terme_recherche']
            print(terme_recherche)
            personnes = Personne.objects.filter(personne__icontains=terme_recherche)
    else:
        form = RecherchePersonneForm()
        personnes = Personne.objects.all()

    context = {
        'personnes': personnes,
        'form': form,
    }
    return render(request, 'myapp_personnes/personne.html', context)



def import_personne(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.cleaned_data['fichier']
            try:
                if uploaded_file.name.endswith('.xlsx'):
                    # Chargez le fichier Excel
                    data = pd.read_excel(uploaded_file)
                elif uploaded_file.name.endswith('.csv'):
                    # Chargez le fichier CSV
                    data = pd.read_csv(uploaded_file)
                else:
                    raise ValueError("Le format de fichier n'est pas pris en charge.")

                for index, row in data.iterrows():
                    nom = row['nom']
                    prenom = row['prenom']
                    # Vérifiez si une personne avec cet email existe déjà
                    personne, created = Personne.objects.get_or_create(nom=nom, prenom=prenom)
                    # Mise à jour des valeurs avec celles du fichier
                    for field in Personne._meta.get_fields():
                        field_name = field.name
                        if field_name in row:
                            setattr(personne, field_name, row[field_name])

                    # Sauvegardez l'enregistrement
                    personne.save()

                messages.success(request, f'Données mises à jour pour {len(data)} personnes.')

            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite : {str(e)}')
        else:
            messages.error(request, f'Veuillez sélectionner un fichier valide.')

    return redirect('admin:myapp_personnes_personne_changelist')  # Mise à jour de la redirection




def personne_view(request):
    personnes = Personne.objects.all().order_by('nom')
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



def custom_404(request, exception):
    return render(request, 'Database/404.html', status=404)


if __name__ == "__main__":
    update_database_from_csv("chemin_vers_votre_fichier.csv")

