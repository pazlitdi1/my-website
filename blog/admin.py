from django.contrib import admin
from blog.models import Blog, Author
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


@admin.register(Blog)
class BlogAdmin(ImportExportModelAdmin):
    list_display = ('id', 'title', 'author', 'created_at',)
    list_display_links = ('id', 'title',)
