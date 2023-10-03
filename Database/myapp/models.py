from django.db import models

class Societe(models.Model):
    societe = models.CharField(max_length=100)
    secteur = models.CharField(max_length=100, null=True, blank=True)
    emails = models.EmailField(max_length=100, null=True, blank=True)
    site_web = models.CharField(max_length=100, null=True, blank=True)
    telephone1 = models.CharField(max_length=20, null=True, blank=True)
    telephone2 = models.CharField(max_length=20, null=True, blank=True)
    telephone3 = models.CharField(max_length=20, null=True, blank=True)
    fixe = models.CharField(max_length=20, null=True, blank=True)
    demarchage = models.BooleanField(default=False)
    demarchage_emails = models.CharField(max_length=100, null=True, blank=True)  # Augmentation de la longueur maximale
    demarchage_numero1 = models.CharField(max_length=20, null=True, blank=True)
    demarchage_numero2 = models.CharField(max_length=20, null=True, blank=True)
    demarchage_numero3 = models.CharField(max_length=20, null=True, blank=True)
    adresse_postal = models.CharField(max_length=10, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    ville = models.CharField(max_length=100, null=True, blank=True)
    pays = models.CharField(max_length=100, null=True, blank=True)
    continent = models.CharField(max_length=100, null=True, blank=True)
    localisation = models.CharField(max_length=255, null=True, blank=True)
    nom = models.CharField(max_length=100, null=True, blank=True)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    sexe = models.CharField(max_length=10, choices=[('masculin', 'Masculin'), ('feminin', 'Féminin')], null=True, blank=True)
    poste = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    tel1 = models.CharField(max_length=20, null=True, blank=True)
    tel2 = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return f"{self.societe} - {self.secteur}{self.site_web}{self.emails}{self.telephone1}{self.prenom}{self.nom}"
