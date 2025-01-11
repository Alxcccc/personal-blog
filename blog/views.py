from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article

class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'blog/article_list.html', context)
