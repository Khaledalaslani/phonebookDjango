from django import forms
from .models import Contact, Number


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name']


class NumberForm(forms.ModelForm):
    class Meta:
        model = Number
        fields = ['number']