
from django.urls import path
from .views import DashboardHomeView, NewslettersDashboardHomeView, NewsletterCreatedView

app_name="dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),  name="home"),
    path('list/',NewslettersDashboardHomeView.as_view(),  name="list"),
    path('created/',NewsletterCreatedView.as_view(),  name="created"),
    
]
