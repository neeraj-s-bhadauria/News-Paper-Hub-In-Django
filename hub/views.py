from django.shortcuts import render
from .models import NewsSites
# Create your views here.


def index(request):
    sites = NewsSites.objects.all()
    return render(request, 'index.html', {'sites': sites})
