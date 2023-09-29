# admin.py
from django.contrib import admin
from .models import Adresse, Personne
import pandas as pd
from django.http import HttpResponseRedirect
from django.urls import path

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email')  # Ajoutez les champs que vous souhaitez afficher dans la liste
    actions = ['import_data']  # Ajoutez une action personnalisée

    def import_data(self, request, queryset):
        # Assurez-vous d'ajuster le chemin vers votre fichier Excel ou CSV
        file_path = 'chemin_vers_votre_fichier.xlsx'  # Remplacez par le chemin de votre fichier

        try:
            # Chargez le fichier Excel ou CSV ici
            data = pd.read_excel(file_path)  # Utilisez 'pd.read_csv' si vous avez un fichier CSV

            for index, row in data.iterrows():
                nom = row['Nom']  # Assurez-vous que 'Nom' correspond au nom de colonne dans le fichier
                prenom = row['Prenom']  # Assurez-vous que 'Prenom' correspond au nom de colonne dans le fichier

                # Recherchez la personne par nom et prénom ou créez-la si elle n'existe pas
                personne, created = Personne.objects.get_or_create(nom=nom, prenom=prenom)

                # Parcourez les colonnes du modèle Personne et mettez à jour les données correspondantes
                for field in Personne._meta.fields:
                    field_name = field.name
                    if field_name in row:
                        setattr(personne, field_name, row[field_name])

                personne.save()

                # Mettez à jour les adresses liées (ManyToMany)
                adresses = row['Adresses']  # Assurez-vous que 'Adresses' correspond au nom de colonne dans le fichier
                adresses = adresses.split(', ')  # Si les adresses sont séparées par des virgules

                personne.adresses.clear()  # Supprime toutes les adresses actuelles liées à la personne

                for adresse in adresses:
                    adresse_obj, created = Adresse.objects.get_or_create(adresse=adresse)
                    personne.adresses.add(adresse_obj)

            self.message_user(request, f'Données mises à jour pour {len(data)} personnes.')  # Affichez un message de succès

        except Exception as e:
            # Gérez les erreurs ici
            self.message_user(request, f'Une erreur s\'est produite : {str(e)}')

    import_data.short_description = 'Importer à partir d\'un fichier Excel/CSV'  # Libellé de l'action

    def import_personne(self, request):
        return HttpResponseRedirect('/admin/import-personne/')  # Redirigez vers la vue d'importation personnalisée

    import_personne.short_description = 'Importer depuis un fichier Excel/CSV'  # Libellé du bouton d'importation

# Enregistrez le modèle personnalisé dans l'administration
admin.site.register(Personne, PersonneAdmin)
admin.site.register(Adresse)
admin.site.register(Personne)


# Définissez l'URL pour la vue d'importation personnalisée
urlpatterns = [
    path('import-personne/', PersonneAdmin.import_personne, name='import_personne'),
]
