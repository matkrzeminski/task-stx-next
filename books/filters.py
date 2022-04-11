from django_filters.filters import DateFromToRangeFilter, CharFilter
from django_filters.rest_framework import FilterSet
from django_filters.widgets import RangeWidget

from .models import Book


class BookFilter(FilterSet):
    title = CharFilter(lookup_expr="icontains", label="Title", field_name="title")
    author = CharFilter(lookup_expr="icontains", label="Author", field_name="author")
    language = CharFilter(
        lookup_expr="iexact", label="Language Code", field_name="language"
    )
    date = DateFromToRangeFilter(
        label="Date Published",
        field_name="published_date",
        widget=RangeWidget(attrs={'placeholder': "YYYY-MM-DD", 'class': "form-group col-xs mb-0"})
    )

    class Meta:
        model = Book
        fields = ("title", "author", "language", "date")
