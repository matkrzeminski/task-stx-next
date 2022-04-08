from django_filters.filters import DateFromToRangeFilter
from django_filters.rest_framework import FilterSet

from .models import Book


class BookFilter(FilterSet):
    published_date = DateFromToRangeFilter()

    class Meta:
        model = Book
        fields = {
            "title": ["icontains"],
            "author": ["icontains"],
            "language": ["iexact"],
            "published_date": [],
        }

    def __init__(self, *args, **kwargs):
        super(BookFilter, self).__init__(*args, **kwargs)
        self.filters["title__icontains"].label = "Title"
        self.filters["author__icontains"].label = "Author"
        self.filters["language__iexact"].label = "Language Code"
