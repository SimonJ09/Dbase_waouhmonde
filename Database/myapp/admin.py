from django.contrib import admin
from .models import  Societe
from django.http import HttpResponseRedirect
from django.urls import path
from django import forms
import pandas as pd

class UploadFileForm(forms.Form):
    fichier = forms.FileField()

class SocieteAdmin(admin.ModelAdmin):
    list_display = ('nom', 'secteur', 'emails')
    actions = ['import_data']
    change_list_template = 'myapp/change_list_upload.html'

    def import_data(self, request, queryset):
        # Récupérez le fichier depuis le formulaire
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid(): 
            uploaded_file = form.cleaned_data['fichier']
            
            try:
                # Chargez le fichier Excel ou CSV ici
                data = pd.read_excel(uploaded_file)  # Utilisez 'pd.read_csv' si vous avez un fichier CSV

                for index, row in data.iterrows():
                    print('test')

                self.message_user(request, f'Données mises à jour pour {len(data)} sociétés.')  # Affichez un message de succès

            except Exception as e:
                self.message_user(request, f'Une erreur s\'est produite : {str(e)}')
        else:
            self.message_user(request, f'Veuillez sélectionner un fichier valide.')

    import_data.short_description = 'Importer à partir d\'un fichier Excel/CSV'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-societe/', self.admin_site.admin_view(self.import_data), name='import_societe_admin'),
        ]
        return my_urls + urls


# Enregistrez le modèle personnalisé dans l'administration
admin.site.register(Societe, SocieteAdmin)
