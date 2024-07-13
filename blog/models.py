

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


class Blog(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=SaveMedia.save_book_image_path, null=True)
    slug = models.SlugField(unique=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True)