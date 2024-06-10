from django.conf import settings

def library_contents(request):

    library_items = []
    total = 0
    article_count = 0

    context = {
        'library_items': library_items,
        'total': total,
        'article_count': article_count,
    }

    return context