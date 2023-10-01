from django.db import models

class Adresse(models.Model):
    postal = models.CharField(max_length=10)
    adresse = models.CharField(max_length=255)
    ville = models.CharField(max_length=100)
    pays = models.CharField(max_length=100)
    continent= models.CharField(max_length=100)
    def __str__(self):
        return f"{self.adresse}, {self.ville}"

class Personne(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    metiers = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    age = models.PositiveIntegerField()
    sexe = models.CharField(max_length=10)
    numero1 = models.CharField(max_length=20)
    numero2 = models.CharField(max_length=20)
    numero3 = models.CharField(max_length=20)
    demarchage_numero1 = models.CharField(max_length=20)
    demarchage_numero2 = models.CharField(max_length=20)
    demarchage_numero3 = models.CharField(max_length=20)
    adresses = models.ManyToManyField(Adresse)  # Utilisez ManyToMany pour plusieurs adresses par personne

    def __str__(self):
        return f"{self.prenom} {self.nom}"
