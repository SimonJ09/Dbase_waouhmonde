from django.urls import path
from . import views

urlpatterns = [
    path('personne/', views.personne_view, name='personne'),
    path('export-personnes-excel/', views.export_personnes_to_excel, name='export-personnes-excel'),
    path('export-personnes-csv/', views.export_personnes_to_csv, name='export-personnes-csv'),
   
]