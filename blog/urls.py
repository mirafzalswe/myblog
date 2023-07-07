from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='blog-home'),
    path('about/', views.about, name='blog-about'),
]