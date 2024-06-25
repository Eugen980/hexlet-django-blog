from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.views import View

from .models import Article


class IndexView(View):  

    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(request, 'articles/index.html', context={
            'articles': articles,
        })

    # def get(self, request, *args, **kwargs):
    #     tags = ['Статья№1', 'Статья№2', 'Статья№3', 'Статья№4']
    #     return render(request, 'articles/index.html', context={'tags': tags})

class ArticleView(View):

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs['id'])
        return render(request, 'articles/show.html', context={
            'article': article,
        })
    
# def index(request, tags, article_id):
#     data = {
#         'tags': tags,
#         'article_id': article_id,
#     }
#     return render(request, 'articles/exapmle.html', data)