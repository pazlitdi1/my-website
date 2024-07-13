from django.urls import path
from .views import home, book, author, book_detail

urlpatterns = [
    path('', home, name='home'),
    path('book/', book, name='book'),
    path('author/', author, name='author'),
    path('book/<slug:slug>/', book_detail, name='book-detail'),

]
