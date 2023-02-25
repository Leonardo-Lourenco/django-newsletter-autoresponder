from django.shortcuts import render
from django.core.checks import messages
from aplicacaonewsletter.models import NewslettersUser
from .forms import NewsletterUserSignUpForm
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def newsletter_signup(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance=form.save(commit=False)

        if NewslettersUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 'This email exists!!!')

        else: 

            instance.save()
            messages.success(request, 'We sendind a message for your email :) ')

            #email
            subject=" News Canal Coffee Tag"
            from_email= settings.EMAIL_HOST_USER
            to_email= [instance.email]

            html_template='newsletter/templates/newsletters/welcome.html'
            html_message= render_to_string(html_template)