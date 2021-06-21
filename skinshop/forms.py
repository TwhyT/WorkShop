from django import forms
from django.db.models import fields
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'Email', 'detail']
        exclude = ['id', 'created', 'update',]