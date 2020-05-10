from django import forms 
from django.contrib.auth.models import User
from .models import Membre
from django.contrib.auth.forms import UserCreationForm


class RegisterMembreForm(UserCreationForm):
    """
    cette classe hérite de UserCreationForm du model User, on utilise pour une meilleure utilisation 
    de création d'un membre
    """
    GENRE = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    email = forms.CharField(label='email', max_length=100)

    genre = forms.ChoiceField(label='genre', choices=GENRE, widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = Membre
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'genre', 'niv_etu', 'filiere']