from django.shortcuts import render

def view_library(request):
    return render(request, 'library/library.html')
