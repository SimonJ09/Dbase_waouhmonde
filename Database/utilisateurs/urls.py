from django.urls import path
from . import views

urlpatterns = [
    path('inscription/', views.inscription, name='inscription'),
    path('connexion/', views.connexion, name='connexion'),
    path('profil/', views.profile_view, name='profil'),
    path('logout/', views.custom_logout, name='custom_logout'),
    # Autres URL liées à l'authentification
]

handler404 = 'utilisateurs.views.custom_404'
