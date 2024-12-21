from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import Contact


class UserForm(forms.ModelForm):
    name = forms.CharField(label='Name', widget=forms.TextInput(attrs={
        'class': 'forms.control','placeholder': 'Nom',
    }))

    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'forms.control','placeholder': 'Email',
    }))

    mes = forms.CharField(label='Message', widget=forms.Textarea(attrs={
        'class': 'forms.control','placeholder': 'Message',
    }))

    class Meta:
        model = Contact
        fields = ('name', 'email', 'mes')
