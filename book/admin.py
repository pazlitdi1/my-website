from django.contrib import admin
from book.models import Book, Author
from import_export.admin import ImportExportModelAdmin


# admin.site.register(Book)
# admin.site.register(Author)


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'created_at',)
    list_display_links = ('id', 'first_name', 'last_name',)
    search_fields = ('id', 'first_name', 'last_name',)
    ordering = ('-created_at',)
    group_by = ('created_at',)


@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'description', 'author', 'price', 'count', 'created_at',)
    list_display_links = ('id', 'title',)



