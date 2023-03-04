from django.shortcuts import render
from django.core.checks import messages
from aplicacaonewsletter.models import NewslettersUser
from .forms import NewsletterUserSignUpForm
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMessage

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
            from_email= settings.EMAIL_HOST_USER  # isso aqui está configurado lá no settings.py
            to_email= [instance.email]

            html_template='newsletters/emails_templates/welcome.html'
            html_message= render_to_string(html_template)
            message=EmailMessage(subject, html_message, from_email, to_email)
            message.content_subtype='html'
            message.send()

    context= {
        'form':form,
    }
    return render(request, 'start-here.html', context)            


# Para a pessoa desiscrever da Lista 
def newsletter_unsubscribe(request):
    form = NewsletterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewslettersUser.objects.filter(email=instance.email).exists(): # Se este email existe na base de dados
            NewslettersUser.objects.filter(email=instance.email).delete()
            messages.success(request, 'Email has been remove with success!! :) ')

        else:
            print('Email not found')
            messages.warning(request, 'Email not found!!')            
    
    context= {
        'form':form,
    }
    return render(request, 'unsubscribe.html', context)     