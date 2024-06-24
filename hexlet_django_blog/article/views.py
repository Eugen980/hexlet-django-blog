from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    tags = ['Статья№1', 'Статья№2', 'Статья№3', 'Статья№4']
    return render(request, 'articles/index.html', context={'tags': tags})
# Create your views here.
