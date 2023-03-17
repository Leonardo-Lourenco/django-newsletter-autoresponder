# Formulário para capitar o email e cadastrar na NEWSLWTTER

from django import  forms
from .models import Newsletter, NewslettersUser

# Capitar o emails da pessoa
class NewsletterUserSignUpForm(forms.ModelForm):
    class Meta:
        model = NewslettersUser
        fields = ['email']

# dados do email que enviamos para a pessoa
class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name', 'subject', 'body', 'email', 'status']