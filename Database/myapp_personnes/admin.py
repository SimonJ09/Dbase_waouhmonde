from django.contrib import admin
from .models import Adresse, Personne
import pandas as pd

admin.site.register(Adresse)
admin.site.register(Personne)

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'numero1')  # Ajoutez les champs que vous souhaitez afficher dans la liste
    actions = ['import_data']  # Ajoutez une action personnalisée

    def import_data(self, request, queryset):
        # Assurez-vous d'ajuster le chemin vers votre fichier Excel ou CSV
        file_path = 'chemin_vers_votre_fichier.xlsx'  # Remplacez par le chemin de votre fichier

        try:
            # Chargez le fichier Excel ou CSV ici
            data = pd.read_excel(file_path)  # Utilisez 'pd.read_csv' si vous avez un fichier CSV

            for index, row in data.iterrows():
                nom_personne = row['Nom']  # Assurez-vous que 'Nom' correspond au nom de colonne dans le fichier
                email = row['Email']  # Assurez-vous que 'Email' correspond au nom de colonne dans le fichier
                numero1 = row['Numero1']  # Assurez-vous que 'Numero1' correspond au nom de colonne dans le fichier

                # Essayez de trouver la personne par son nom
                personne, created = Personne.objects.get_or_create(nom=nom_personne)

                # Mettez à jour les colonnes
                personne.email = email
                personne.numero1 = numero1
                personne.save()

            self.message_user(request, f'Données mises à jour pour {len(data)} personnes.')  # Affichez un message de succès

        except Exception as e:
            # Gérez les erreurs ici
            self.message_user(request, f'Une erreur s\'est produite : {str(e)}')

    import_data.short_description = 'Importer à partir d\'un fichier Excel/CSV'  # Libellé de l'action

# Enregistrez le modèle personnalisé dans l'administration
admin.site.register(Personne, PersonneAdmin)


from django.urls import path
from django.http import HttpResponseRedirect

class PersonneAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'numero1')  # Ajoutez les champs que vous souhaitez afficher dans la liste

    def import_data(self, request):
        return HttpResponseRedirect('/admin/import-data/')  # Redirigez vers la vue d'importation personnalisée

    import_data.short_description = 'Importer depuis un fichier Excel/CSV'  # Libellé du bouton d'importation

# Enregistrez le modèle personnalisé dans l'administration
admin.site.register(Personne, PersonneAdmin)

# Définissez l'URL pour la vue d'importation personnalisée
urlpatterns = [
    path('import-data/', import_data_view, name='import_data'),
]

