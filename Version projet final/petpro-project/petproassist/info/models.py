from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django_comments_xtd.models import XtdComment as Comment
#from django_comments_xtd.models import Comment
from django.contrib.contenttypes.fields import GenericRelation
#from django_comments_xtd import comments
#from django.contrib.comments.models import Comment
from django import forms
from django.shortcuts import render
from django.conf import settings
from django.utils import timezone


class UtilisateurPersonnalise(AbstractUser):
    # Champs supplémentaires
    age = models.IntegerField(blank=True, null=True)  # ajouter des contraintes si nécessaire
    adresse = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.username  # choisir un champ différent pour la représentation de l'utilisateur

    class Meta:
        verbose_name = 'Utilisateur Personnalisé'
        verbose_name_plural = 'Utilisateurs Personnalisés'

class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adresse_ville = models.CharField(max_length=255)
    numero_telephone = models.CharField(max_length=15)
    photo_de_profil = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    profile_completed = models.BooleanField(default=False)  # Champ pour indiquer si le profil est complet

    def __str__(self):
        return self.user.username

class Animal(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom

class Service(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom   

class Proprietaire(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)  # Vous pouvez créer un modèle Adresse séparé
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15)
    animaux = models.ManyToManyField(Animal, choices=(
        ('chien', 'Chien'),
        ('chat', 'Chat'),
        ('poule', 'Poule'),
        ('oiseau', 'Oiseau'),
        ('lapin', 'Lapin'),
        ('poisson', 'Poisson'),
        ('autre', 'Autre'),
    ))
    besoins = models.ManyToManyField('Service', related_name='proprietaires')
    commentaire = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username

    
class Prestataire(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=255)
    prenoms = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255) 
    email = models.EmailField(unique=True)
    numero_telephone = models.CharField(max_length=15)
    type_services = models.ManyToManyField(Service, related_name='prestataires')
    tarifs = models.DecimalField(max_digits=10, decimal_places=2) #choice
    references = models.DecimalField(max_digits=3, decimal_places=2)
    commentaire = models.TextField(max_length=200)

    def __str__(self):
        return self.user.username


class Publication(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    tarif = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content[:75]
    # Ajoutez d'autres champs comme la date de publication.

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication = models.ForeignKey('Publication', on_delete=models.CASCADE)  # Remplacez 'Publication' par le nom de votre modèle de publication
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Commentaire de {self.user} sur {self.content[:75]}"

#class Tarif(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  service_name = models.CharField(max_length=100)
   # price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs comme la description du service.

#class Message(models.Model):
 #   sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
  #  receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
   # content = models.TextField()
    # Ajoutez d'autres champs comme la date et l'heure du message.

class Message(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver')
    content = models.TextField()
    # Ajoutez d'autres champs comme la date et l'heure du message.

    def __str__(self):
        return f"De {self.sender} à {self.receiver}"

    
 # Ajoutez d'autres champs
#class Comment(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  publication = models.ForeignKey(Publication, on_delete=models.CASCADE)
   # content = models.TextField()
    # Ajoutez d'autres champs comme la date du commentaire.

   # def __str__(self):
    #    return f"Commentaire de {self.user} sur {self.publication}"

#Sclass Tarif(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  service_name = models.CharField(max_length=100)
   # price = models.DecimalField(max_digits=10, decimal_places=2)
    #description = models.TextField()
#
 #   def __str__(self):
  #      return self.service_name
