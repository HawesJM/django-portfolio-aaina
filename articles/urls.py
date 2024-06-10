
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('add/', views.add_article, name='add_article'),
]
