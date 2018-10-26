from django.shortcuts import render,get_object_or_404
from .models import Gallary

# Create your views here.
def home(request):
    gallarys = Gallary.objects
    return render(request, "home.html", {'gallarys': gallarys})

def page(request, gallary_id):
    page = get_object_or_404(Gallary, pk=gallary_id)
    return render(request, 'page.html', {'page': page})
