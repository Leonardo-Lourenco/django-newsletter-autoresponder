# Formulário para capitar o email e cadastrar na NEWSLWTTER

from django import  forms
from .models import Newsletter, NewslettersUser

class NewsletterUserSignUpForm(forms.ModelForm):
    class meta:
        model = NewslettersUser
        filter = ['email']


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'subject', 'body', 'email']