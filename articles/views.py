from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Article, Category
from .forms import ArticleForm


def all_articles(request):

    articles = Article.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            articles = articles.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "you've entered no search crieteria")
                return redirect(reverse("articles"))

            queries = Q(name__icontains=query) | Q(keywords__icontains=query)
            articles = articles.filter(queries)

    context = {
        'articles': articles,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, "articles/articles.html", context)

def add_article(request):
    form = ArticleForm()
    template = 'articles/add_article.html'
    context = {
        'form': form,
    }

    return render(request, template, context)