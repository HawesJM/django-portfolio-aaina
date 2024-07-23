from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Talk
from django.views.generic import ListView
from django.core.paginator import Paginator

def all_talks(request):

    talks = Talk.objects.all()

    context = {
        'talks':talks
    }

    return render(request, "talks/talks.html", context)

    page = request.GET.get('page', 1)
    paginator = Paginator(talks, 20)
    try:
        talks = paginator.page(page)
    except PageNotAnInteger:
        talks = paginator.page(1)
    except EmptyPage:
        talks = paginator.page(paginator.num_pages)