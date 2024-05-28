from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'published_date',
        'category',
        'keywords',
        'url',
        'image',
        'image_url',
    )
    ordering = ('published_date',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)