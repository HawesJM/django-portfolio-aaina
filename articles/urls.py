
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_articles, name='articles'),
    path('add/', views.add_article, name='add_article'),
    path('edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('delete/<int:article_id>/', views.delete_article, name='delete_article'),
]
