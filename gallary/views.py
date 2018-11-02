from django.shortcuts import render, get_object_or_404
from .models import Gallary
from account.models import Article

# Create your views here.


def home(request):
    gallarys = Gallary.objects
    articles = Article.objects
    return render(request, "home.html", {'gallarys': gallarys, 'articles': articles})


def page(request, gallary_id):
    page = get_object_or_404(Gallary, pk=gallary_id)
    return render(request, 'page.html', {'page': page})
