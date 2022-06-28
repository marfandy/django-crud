from random import choices
from django import forms
from api import models


class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    gender = forms.CharField(
        label='Gander', max_length=100, choices=models.Gender.choices)
