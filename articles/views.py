from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Article


def all_articles(request):

    articles = Article.objects.all()

    query = None

    if request.GET:
        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "you've entered no search crieteria")
                return redirect(reverse("articles"))

            queries = Q(title__icontains=query) | Q(keywords__icontains=query)
            articles = articles.filter(queries)

    context = {
        "articles": articles,
        "search_term": query,
    }

    return render(request, "articles/articles.html", context)
