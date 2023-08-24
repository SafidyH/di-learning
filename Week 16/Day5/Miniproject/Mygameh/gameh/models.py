from django.db import models
from django.contrib.auth.models import User
from django.db import models

class HighScore(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()

    def __str__(self):
        return f"{self.player.username} - Score: {self.score}"

class Word(models.Model):
    word_text = models.CharField(max_length=50)
    word_length = models.IntegerField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.word_text