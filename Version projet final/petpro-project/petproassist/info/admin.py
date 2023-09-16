from django.contrib import admin
from .models import Profil, Animal, Service, Proprietaire, Prestataire, Publication, Message, Comment #, #AutreModele1, AutreModele2, Tarif
from django_comments_xtd.models import XtdComment as Comment
from django_comments_xtd.models import Comment
# Classe d'administration pour le modèle Profil
#class ProfilAdmin(admin.ModelAdmin):
    #list_display = ['user', 'adresse_ville', 'numero_telephone']  # Configurez les champs à afficher dans la liste des objets

@admin.register(Profil)
class ProfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'adresse_ville', 'numero_telephone', 'photo_de_profil', 'profile_completed')

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('nom',)

@admin.register(Proprietaire)
class ProprietaireAdmin(admin.ModelAdmin):
    list_display = ('user', 'nom', 'prenoms', 'adresse', 'email', 'numero_telephone', 'commentaire')

@admin.register(Prestataire)
class PrestataireAdmin(admin.ModelAdmin):
    list_display = ('user', 'nom', 'prenoms', 'adresse', 'email', 'numero_telephone', 'tarifs', 'references', 'commentaire')

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('user', 'content')

#@admin.register(Tarif)
#class TarifAdmin(admin.ModelAdmin):
 #   list_display = ('user', 'service_name', 'price', 'description')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'content')
'''
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'date_created')
'''

# Classe d'administration pour les autres modèles
#class AutreModele1Admin(admin.ModelAdmin):
    # Configurez les options d'administration pour AutreModele1

#class AutreModele2Admin(admin.ModelAdmin):
    # Configurez les options d'administration pour AutreModele2

# Enregistrez les classes d'administration
#admin.site.register(Profil, ProfilAdmin)
    #admin.site.register(AutreModele1, AutreModele1Admin)
    #Eadmin.site.register(AutreModele2, AutreModele2Admin)
