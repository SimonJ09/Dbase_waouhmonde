from django.db import models

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)  # Utilisation de PositiveIntegerField pour l'âge
    sexe = models.CharField(max_length=10, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], null=True, blank=True)  # Champ "sexe" avec choix
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)
    tel3 = models.CharField(max_length=20, null=True, blank=True)
    demarchage_tel1 = models.CharField(max_length=20, null=True, blank=True)
    demarchage_tel2 = models.CharField(max_length=20, null=True, blank=True)
    demarchage_tel3 = models.CharField(max_length=20, null=True, blank=True)
    postal = models.CharField(max_length=10, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    continent = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return f"{self.prenom} {self.nom} {self.email} {self.poste}"
