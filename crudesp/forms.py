from dataclasses import fields
from django import forms
from .models import especialista

class especialistaForm(forms.ModelForm):
    class Meta:
        model=especialista
        fields='__all__'