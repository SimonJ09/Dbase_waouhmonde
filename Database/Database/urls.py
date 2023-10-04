
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from myapp.admin import SocieteAdmin


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.accueil, name='accueil'), 
    path('apropos/', views.propos, name='propos'), 
    path('homes/', views.homes, name='homes'),
    path("contact/", views.contact_view, name='contact'),
    path('', include('myapp.urls')), 
    path('', include('myapp_personnes.urls')), 
    path('utilisateur/', include('utilisateurs.urls')), 
  
]

handler404 = 'Database.views.custom_404'

