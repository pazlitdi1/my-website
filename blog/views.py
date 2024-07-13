from django.shortcuts import render
from .models import Author, Blog
from django.contrib.auth.decorators import login_required


def author(request):
    authors = Author.objects.all()
    return render(request, 'author.html', {'authors': authors})


@login_required(login_url='login')
def blog(request):
    if request.method == 'POST':
        search = request.POST['search']
        blogs = Blog.objects.filter(title__icontains=search)
        if len(blogs) != 0:
            return render(request, 'book.html', {'blogs': blogs, "value": search, "message": "Blog found"})
        else:
            return render(request, 'book.html', {'blogs': blogs, "value": search, "message": "Blog not found"})

    blogs = Blog.objects.all()
    return render(request, 'book.html', {'blogs': blogs})


def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    if blog:
        return render(request, 'blog_detail.html', {'blog': blog,  "message": "Book found"})

    else:
        return render(request, 'blog_detail.html', {'blog': blog, "message": "Book not found"})