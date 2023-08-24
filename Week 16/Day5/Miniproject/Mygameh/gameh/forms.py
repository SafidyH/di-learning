from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    # Personnalisez les champs si nécessaire
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    # Personnalisez les champs si nécessaire
    pass
from django import forms

class WordGuessForm(forms.Form):
    guess = forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )