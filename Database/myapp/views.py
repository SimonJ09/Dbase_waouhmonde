# views.py
from django.shortcuts import render, redirect
from .models import Societe
import pandas as pd
from django.http import HttpResponse
from myapp.models import Societe
import csv
from django.contrib import messages
from .forms import UploadFileForm
from .forms import RechercheSocieteForm

def recherche_societe(request):
    if request.method == 'POST':
        print('ok')
        form = RechercheSocieteForm(request.POST)
        print(('ok'))
        if form.is_valid():
            terme_recherche = form.cleaned_data['terme_recherche']
            societes = Societe.objects.filter(societe__icontains=terme_recherche)
    else:
        form = RechercheSocieteForm()
        societes = Societe.objects.all()

    context = {
        'societes': societes,
        'form': form,
    }

    return render(request, 'myapp/societe.html', context)
 


def import_societe(request):
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

                # Get the columns available in the uploaded file
                available_columns = data.columns

                for index, row in data.iterrows():
                    emails = row['emails']
                    # Vérifiez si une personne avec cet email existe déjà
                    societe, created = Societe.objects.get_or_create(emails=emails)

                    # Mise à jour des valeurs avec celles du fichier
                    model_fields = [field.name for field in Societe._meta.get_fields()]
                    for field_name in available_columns:
                        if field_name in model_fields:
                            setattr(societe, field_name, row[field_name])

                    # Sauvegardez l'enregistrement
                    societe.save()

                messages.success(request, f'Données mises à jour pour {len(data)} personnes.')

            except Exception as e:
                messages.error(request, f'Une erreur s\'est produite : {str(e)}')
        else:
            messages.error(request, f'Veuillez sélectionner un fichier valide.')

    return redirect('admin:myapp_societe_changelist')



def home_view(request):
    return render(request, 'myapp/home.html')

def societe_view(request):
    societes = Societe.objects.all().order_by('societe')
    context = {
        'societes': societes
    }
    return render(request, 'myapp/societe.html', context)



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
    societes = Societe.objects.all().order_by('societe')

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



def custom_404(request, exception):
    return render(request, 'Database/404.html', status=404)