from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth import get_user_model

class CustomUser(AbstractUser):
    # Ajoutez des champs personnalisés ici
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.user.date_of_birth} {self.user.profile_picture }{self.user.bio}"

