from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleEditAdminView, ArticleCreateAdminView, ArticleDeleteAdminView

app_name = 'blog'

urlpatterns = [
    
    path('', ArticleListView.as_view(), name='home'),
    path('article/<int:id_article>', ArticleDetailView.as_view(), name='detail'),
    path('article/edit/<int:pk>', ArticleEditAdminView.as_view(), name='update'),
    path('article/new', ArticleCreateAdminView.as_view(), name='create'),
    path('article/delete/<int:pk>', ArticleDeleteAdminView.as_view(), name='delete')
]