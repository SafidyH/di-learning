from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
import random

class User(AbstractUser):
    amount_of_money = models.PositiveIntegerField(default=1000)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        # Add a unique app_label to prevent clashes with the auth app
        app_label = 'cards'

def random_price():
    return random.randint(200, 2000)

def random_xp_points():
    return random.randint(1, 10)

class Card(models.Model):
    name_character = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    house = models.CharField(max_length=50)
    image_url = models.URLField()
    date_of_birth = models.DateField(null=True, blank=True)
    patronus = models.CharField(max_length=50)
    price = models.PositiveIntegerField(default= random_price)
    xp_points = models.PositiveIntegerField(default=random_xp_points)
    current_owner = models.ForeignKey(User, related_name='cards_owned', on_delete=models.SET_NULL, null=True, blank=True)
    previous_owner = models.ForeignKey(User, related_name='cards_previously_owned', on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return self.name_character
    

    # Define a related_name for groups and user_permissions fields
User._meta.get_field('groups').remote_field.related_name = 'cards_user_groups'
User._meta.get_field('user_permissions').remote_field.related_name = 'cards_user_permissions'
