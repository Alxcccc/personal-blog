from django.contrib import admin
from django.urls import path, include

from .views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', HomeView.as_view(), name="Home"),
    
    path('accounts/', include('django.contrib.auth.urls'), name="Accounts"),
    
    path('blog/', include('blog.urls', namespace='blog')),
]
