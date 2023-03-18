
from django.urls import path
from .views import DashboardHomeView, NewslettersDashboardHomeView, NewsletterCreatedView, NewsletterDetailView, NewsletterUpdateView

app_name="dashboard"

urlpatterns = [
    path('',DashboardHomeView.as_view(),  name="home"),
    path('list/',NewslettersDashboardHomeView.as_view(),  name="list"),
    path('created/',NewsletterCreatedView.as_view(),  name="created"),
    path('detail/<int:pk>',NewsletterDetailView.as_view(),  name="detail"),
    path('update/<int:pk>',NewsletterUpdateView.as_view(),  name="update"),
    
]
