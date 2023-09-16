import random
import requests
from django.core.management.base import BaseCommand
from cards.models import Card, User

class Command(BaseCommand):
    help = 'Fetch data from the Harry Potter API and populate the Card model'

    def handle(self, *args, **options):
        # Assuming you have a single User instance
        #user = User.objects.get(username='Safidy') #your_username
        
        user, created = User.objects.get_or_create(
            username='Hasina',  # Replace with your desired username
            defaults={'email': 'safidyhasina03@gmail.com'}  # Replace with your desired email
        )
        url = 'https://hp-api.onrender.com/api/characters'  # Replace with the actual API endpoint https://hp-api.onrender.com/api/characters/students ou https://hp-api.onrender.com/harrypotter/cards

        response = requests.get(url)
        data = response.json()

        for card_data in data:
            card = Card.objects.create(
                name_character=card_data['name'],
                species=card_data['species'],
                house=card_data['house'],
                image_url=card_data['image'],
                patronus=card_data['patronus'],
                date_of_birth=card_data.get('date_of_birth'),
                price=random.randint(200, 2000),
                xp_points=random.randint(1, 10),
                current_owner=user,
            )
            self.stdout.write(self.style.SUCCESS(f'Created card: {card.name_character}'))
