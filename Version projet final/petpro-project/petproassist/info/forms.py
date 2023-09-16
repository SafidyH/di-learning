from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profil, Proprietaire, Prestataire, Service, Animal, Publication, Message  #, Comment, Tarif,
from .models import Comment as CommentModel
from django.contrib.auth.forms import AuthenticationForm
from django.db import models
#from django.contrib.contenttypes.fields import GenericRelation
#from .models import Publication as PublicationModel
#from .models import Tarif as TarifModel 
from django_comments_xtd.models import XtdComment as Comment
#from django_comments_xtd.models import Comment

class CustomAuthenticationForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=[('prestataire', 'Prestataire'), ('proprietaire', 'Propriétaire')], required=True, widget=forms.RadioSelect)

class UserRegistrationForm(UserCreationForm):
   
    statut = forms.ChoiceField(choices=[('proprietaire', 'Propriétaire'), ('prestataire', 'Prestataire')])
    first_name = forms.CharField(max_length=30, required=True, help_text='Requis. Entrez votre prénom.')
    last_name = forms.CharField(max_length=30, required=True, help_text='Requis. Entrez votre nom de famille.')
    email = forms.EmailField(max_length=254, required=True, help_text='Requis. Entrez une adresse email valide.')
    password1 = forms.CharField(
        label="Mot de passe",
        widget=forms.PasswordInput,
        help_text="Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être trop courant."
    )
    password2 = forms.CharField(
        label="Confirmez le mot de passe",
        widget=forms.PasswordInput,
        help_text="Entrez le même mot de passe que ci-dessus, pour vérification."
    )
    STATUT_CHOICES = (
        ('proprietaire', 'Propriétaire'),
        ('prestataire', 'Prestataire de service'),
    )
    statut = forms.ChoiceField(choices=STATUT_CHOICES, required=True, help_text='Choisissez votre statut.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        help_texts = {
            'username': 'Requis. 150 caractères maximum. Lettres, chiffres et @/./+/-/_ uniquement.',
            'password1': 'Votre mot de passe doit contenir au moins 8 caractères et ne peut pas être trop courant.',
            'password2': 'Entrez le même mot de passe que ci-dessus, pour vérification.'
        }

    #class Meta:
       # model = User
        #fields = ['username', 'last_name', 'first_name', 'email', 'statut', 'password1', 'password2']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['adresse_ville', 'numero_telephone', 'photo_de_profil', 'profile_completed']

class ProprietaireForm(forms.ModelForm):
    class Meta:
        model = Proprietaire
        fields = ['animaux', 'besoins', 'commentaire']

class PrestataireForm(forms.ModelForm):
    class Meta:
        model = Prestataire
        fields = ['type_services', 'tarifs', 'references', 'commentaire']

class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['nom']
'''
class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nom']

'''
#class PublicationForm(forms.ModelForm):
 #   class Meta:
  #      model = PublicationModel  # Utilisez l'alias pour le modèle
    #    fields = ['content', 'tarif'] 

#class Publication(models.Model):
    # Champs de votre modèle Publication
  #  titre = models.CharField(max_length=100)
   # contenu = models.TextField()
    # ...

    # Ajoutez GenericRelation pour activer les commentaires
  #  comments = GenericRelation(Comment)

#    def __str__(self):
  #      return self.titre
    
#class PublicationSearchForm(forms.Form):
 #   search_query = forms.CharField(max_length=100, required=False, label='Rechercher des publications')


#class TarifForm(forms.ModelForm):
   # class Meta:
   #     model = Tarif
   #     fields = ['service_name', 'price']  # Ajoutez d'autres champs

#class Tarif(models.Model):
 #   user = models.ForeignKey(User, on_delete=models.CASCADE)
  #  service_name = models.CharField(max_length=100)
   # price = models.DecimalField(max_digits=10, decimal_places=2)
    # Ajoutez d'autres champs comme la description du service.

    #def __str__(self):
     #   return self.service_name
    
    
#class TarifForm(forms.ModelForm):
 #   class Meta:
  #      model = TarifModel  # Utilisez l'alias pour le modèle
   #     fields = ['service_name', 'price', 'description']  


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['content']  # Ajoutez d'autres champs


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['content']  # Ajoutez d'autres champs


#class CommentForm(forms.ModelForm):
  #  class Meta:
      #  model = Comment
      #  fields = ['content'] 

