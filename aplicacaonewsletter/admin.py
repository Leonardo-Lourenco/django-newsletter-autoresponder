from django.contrib import admin

from .models import NewslettersUser,Newsletter

# Register your models here.
admin.site.register(NewslettersUser)
admin.site.register(Newsletter)