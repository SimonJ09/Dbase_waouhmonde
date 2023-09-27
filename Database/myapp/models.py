from django.db import models

class Adresse(models.Model):
    postal = models.CharField(max_length=10)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    continent = models.CharField(max_length=100)
    localisation = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.adresse}, {self.ville}"

class Decideur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    poste = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    numero1 = models.CharField(max_length=20)
    numero2 = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Societe(models.Model):
    nom = models.CharField(max_length=100)
    secteur = models.CharField(max_length=100)
    emails = models.EmailField(max_length=100)
    numero1 = models.CharField(max_length=20)
    numero2 = models.CharField(max_length=20)
    numero3 = models.CharField(max_length=20)
    fixe = models.CharField(max_length=20)
    adresses = models.ManyToManyField(Adresse, related_name='societes_adresse')  # Utilisez un nom de requête inversée personnalisé
    adresse_postal = models.OneToOneField(Adresse, on_delete=models.CASCADE, related_name='societe_adresse_postal')  # Utilisez un nom de requête inversée personnalisé
    demarchage_emails = models.EmailField(max_length=100)
    demarchage_numero1 = models.CharField(max_length=20)
    demarchage_numero2 = models.CharField(max_length=20)
    demarchage_numero3 = models.CharField(max_length=20)
    decideurs = models.ManyToManyField(Decideur, related_name='societes_decideurs')  # Utilisez un nom de requête inversée personnalisé

    def __str__(self):
        return self.nom
