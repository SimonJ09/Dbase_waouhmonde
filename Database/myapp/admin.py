from django.contrib import admin
from .models import Adresse, Decideur, Societe

admin.site.register(Decideur)
admin.site.register(Adresse)
admin.site.register(Societe)