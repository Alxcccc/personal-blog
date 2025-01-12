from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Article
from .forms import ArticleCreateForm

class ArticleListView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        context = {
            'articles': articles,
        }
        return render(request, 'blog/article_list.html', context)
    
class ArticleDetailView(View):
    def get(self, request, id_article, *args, **kwargs):
        article = get_object_or_404(Article, pk=id_article)
        context = {
            'article': article
        }
        return render(request, 'blog/article_detail.html', context)

class ArticleCreateAdminView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleCreateForm()
        context = {
            'form': form
        }
        return render(request, 'blog/article_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = ArticleCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')
                
                p, created = Article.objects.get_or_create(title=title, defaults={'content': content})
                p.save()
                return redirect('blog:home')
        context = {
            
        }
        return render(request, 'blog/article_create.html', context)
    
class ArticleEditAdminView(UpdateView):
    model = Article
    fields = ['title', 'content']
    template_name = 'blog/article_update.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
class ArticleDeleteAdminView(DeleteView):
    model = Article
    template_name='blog/article_delete.html'
    def get_success_url(self):
        return reverse_lazy('blog:home')
    
    

