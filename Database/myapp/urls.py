from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('societe/', views.societe_view, name='societe'),
    path('export-societe-excel/', views.export_societe_to_excel, name='export-societe-excel'),
    path('export-societe-csv/', views.export_societe_to_csv, name='export-societe-csv'),
]
