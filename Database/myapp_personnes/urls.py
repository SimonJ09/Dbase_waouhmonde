from django.urls import path
from . import views
from . import admin


urlpatterns = [
    path('personne/', views.personne_view, name='personne'),
    path('seck_personne/', views.recherche_personne, name='recherche_personne'),
    path('import-personne/', views.import_personne, name='import_personne'),
    path('export-personnes-excel/', views.export_personnes_to_excel, name='export-personnes-excel'),
    path('export-personnes-csv/', views.export_personnes_to_csv, name='export-personnes-csv'),
   
]

handler404 = 'myapp_personnes.views.custom_404'