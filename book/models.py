

from django.db import models
from django.contrib.auth.models import User
from .helpers import SaveMedia


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    birt_date = models.DecimalField
    created_at = models.DateTimeField(auto_now_add=True)

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.get_full_name()


class Book(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books', null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    slug = models.SlugField(unique=True, null=False)
    price = models.DecimalField(max_digits=5, decimal_places=2,)
    count = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comments(models.Model):
    users = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    book = models.ManyToManyField(Book)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class WishlistBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wishlist_books', null=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title