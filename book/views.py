from django.shortcuts import render
from .models import Author, Book
from django.contrib.auth.decorators import login_required


def author(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


def book(request):
    if request.method == 'POST':
        search = request.POST['search']
        books = Book.objects.filter(title__icontains=search)
        if len(books) != 0:
            return render(request, 'book.html', {'books': books, "value": search, "message": "Book found"})
        else:
            return render(request, 'book.html', {'books': books, "value": search, "message": "Book not found"})

    books = Book.objects.all()
    return render(request, 'book.html', {'books': books})


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def book_detail(request, slug):
    book = Book.objects.get(slug=slug)
    if book:
        return render(request, 'book_detail.html', {'book': book,  "message": "Book found"})

    else:
        return render(request, 'book_detail.html', {'book': book, "message": "Book not found"})

