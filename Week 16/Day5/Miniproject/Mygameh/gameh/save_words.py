import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "countdown_game.settings")
django.setup()

from countdown.models import Word
word_list = ["apple", "banana", "cherry", "grape", "orange", "strawberry"]
for word in word_list:
    Word.objects.create(word_text=word, word_length=len(word), category="fruit")
    print(f"Word '{word}' saved to the database.")