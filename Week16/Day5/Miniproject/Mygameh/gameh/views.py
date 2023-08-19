from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, LoginForm

import random
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WordGuessForm
from .models import Word, HighScore

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('game')  # Redirige vers la vue du jeu
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('game')  # Redirige vers la vue du jeu
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige vers la page de connexion




class CountdownGameView(LoginRequiredMixin, View):
    template_name = 'countdown/game.html'
    form_class = WordGuessForm

    def get(self, request, *args, **kwargs):
        shuffled_word = self.get_random_word()
        form = self.form_class()
        context = {'shuffled_word': shuffled_word, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        shuffled_word = self.get_random_word()
        form = self.form_class(request.POST)
        guess = form['guess'].value()
        score = self.calculate_score(shuffled_word, guess)
        self.save_score(request.user, score)
        total_score = HighScore.objects.filter(player=request.user).aggregate(total_score=models.Sum('score'))['total_score']
        context = {'shuffled_word': shuffled_word, 'form': form, 'score': score, 'total_score': total_score}
        return render(request, self.template_name, context)

    def get_random_word(self):
        word = random.choice(Word.objects.filter(word_length__gte=6))
        return self.shuffle_word(word.word_text)

    def shuffle_word(self, word):
        shuffled_word = list(word)
        random.shuffle(shuffled_word)
        return ''.join(shuffled_word)

    def calculate_score(self, shuffled_word, guess):
        if guess == shuffled_word:
            return 10
        elif guess == Word.objects.filter(word_length=len(shuffled_word)).order_by('-word_length').first().word_text:
            return 8
        elif guess == Word.objects.filter(word_length=len(shuffled_word)-1).order_by('-word_length').first().word_text:
            return 5
        elif guess == Word.objects.filter(word_length=len(shuffled_word)-2).order_by('-word_length').first().word_text:
            return 3
        else:
            return 0

    def save_score(self, player, score):
        HighScore.objects.create(player=player, score=score)
