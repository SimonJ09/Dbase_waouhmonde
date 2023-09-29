# admin.py
from django.contrib import admin
from .models import Adresse, Decideur, Societe
import pandas as pd
from django.http import HttpResponseRedirect
from django.urls import path

class SocieteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'emails')  # Ajoutez les champs que vous souhaitez afficher dans la liste
    actions = ['import_data']  # Ajoutez une action personnalisée

    def import_data(self, request, queryset):
        # Assurez-vous d'ajuster le chemin vers votre fichier Excel ou CSV
        file_path = 'chemin_vers_votre_fichier.xlsx'  # Remplacez par le chemin de votre fichier

        try:
            # Chargez le fichier Excel ou CSV ici
            data = pd.read_excel(file_path)  # Utilisez 'pd.read_csv' si vous avez un fichier CSV

            for index, row in data.iterrows():
                nom_societe = row['Nom']  # Assurez-vous que 'Nom' correspond au nom de colonne dans le fichier

                # Recherchez l'entreprise par son nom ou créez-la si elle n'existe pas
                societe, created = Societe.objects.get_or_create(nom=nom_societe)

                # Parcourez les colonnes du modèle Societe et mettez à jour les données correspondantes
                for field in Societe._meta.fields:
                    field_name = field.name
                    if field_name in row:
                        setattr(societe, field_name, row[field_name])

                societe.save()

                # Mettez à jour les adresses liées (ManyToMany)
                adresses = row['Adresses']  # Assurez-vous que 'Adresses' correspond au nom de colonne dans le fichier
                adresses = adresses.split(', ')  # Si les adresses sont séparées par des virgules

                societe.adresses.clear()  # Supprime toutes les adresses actuelles liées à la société

                for adresse in adresses:
                    adresse_obj, created = Adresse.objects.get_or_create(adresse=adresse)
                    societe.adresses.add(adresse_obj)

                # Mettez à jour les décideurs liés (ManyToMany)
                decideurs = row['Decideurs']  # Assurez-vous que 'Decideurs' correspond au nom de colonne dans le fichier
                decideurs = decideurs.split(', ')  # Si les décideurs sont séparés par des virgules

                societe.decideurs.clear()  # Supprime tous les décideurs actuels liés à la société

                for decideur in decideurs:
                    nom, prenom = decideur.split(' ')  # Si le nom et le prénom sont séparés par un espace
                    decideur_obj, created = Decideur.objects.get_or_create(nom=nom, prenom=prenom)
                    societe.decideurs.add(decideur_obj)

            self.message_user(request, f'Données mises à jour pour {len(data)} sociétés.')  # Affichez un message de succès

        except Exception as e:
            # Gérez les erreurs ici
            self.message_user(request, f'Une erreur s\'est produite : {str(e)}')

    import_data.short_description = 'Importer à partir d\'un fichier Excel/CSV'  # Libellé de l'action

    def import_societe(self, request):
        return HttpResponseRedirect('/admin/import-societe/')  # Redirigez vers la vue d'importation personnalisée

    import_societe.short_description = 'Importer depuis un fichier Excel/CSV'  # Libellé du bouton d'importation

# Enregistrez le modèle personnalisé dans l'administration
admin.site.register(Societe, SocieteAdmin)
admin.site.register(Adresse)
admin.site.register(Societe)
admin.site.register(Decideur)



