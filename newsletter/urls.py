
from django.contrib import admin
from django.urls import path, include
from .views import  base

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',base, name='base'),
    path('newsletter/', include('aplicacaonewsletter.urls', namespace='aplicacaonewsletter')),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
]
