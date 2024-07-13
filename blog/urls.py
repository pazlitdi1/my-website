from django.urls import path
from .views import home, blog, author, blog_detail

urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name='blog'),
    path('author/', author, name='author'),
    path('blog/<slug:slug>/', blog_detail, name='blog-detail')]

