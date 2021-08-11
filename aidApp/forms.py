from django.db.models.base import Model
from django.forms import ModelForm

from .models import ContactUs, Newsletter


class ContactUsForm(ModelForm):
    class Meta:
        model = ContactUs
        fields = ['first_name', 'last_name', 'email', 'message']


class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'email']
