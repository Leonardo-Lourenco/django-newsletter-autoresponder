
from django.contrib import admin
from django.urls import path
from .views import newsletter_signup, newsletter_unsubscribe

app_name="aplicacaonewsletter"

urlpatterns = [
    path('sigup/',newsletter_signup,  name="sigup" ),
    path('unsubscribe/',newsletter_unsubscribe,  name="unsubscribe" ),
]
