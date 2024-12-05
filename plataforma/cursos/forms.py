from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Curso

class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, help_text='Nome completo')

    class Meta:
        model = User
        fields = ('username', 'full_name', 'password1', 'password2')