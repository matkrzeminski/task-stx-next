from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn', 'pages', 'language')
    list_filter = ('published_date', 'language')
    search_fields = ('title', 'author', 'isbn', 'published_date')
    date_hierarchy = 'published_date'
    ordering = ('-published_date',)
