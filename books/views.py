from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, FormView, DeleteView
from django_filters.rest_framework import DjangoFilterBackend
from django_filters.views import FilterView
from rest_framework import generics, permissions

from .filters import BookFilter
from .forms import BookImportForm, BookForm
from .models import Book
from .serializers import BookSerializer
from .utils import import_book_data


class BookFilterView(FilterView):
    filterset_class = BookFilter
    template_name = "books/book_filter.html"


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:filter")


class BookDeleteView(DeleteView):
    model = Book
    template_name = "books/book_confirm_delete.html"
    success_url = reverse_lazy("books:filter")
    context_object_name = "book"


class BookUpdateView(UpdateView):
    model = Book
    form_class = BookForm
    template_name = "books/book_form.html"
    success_url = reverse_lazy("books:filter")


class BookListAPIView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter


class BookImportView(FormView):
    template_name = "books/book_import.html"
    form_class = BookImportForm
    success_url = reverse_lazy("books:filter")

    def form_valid(self, form):
        book_data = import_book_data(**form.cleaned_data)
        if not book_data:
            form.add_error(None, "No books found.")
            return self.form_invalid(form)
        Book.objects.create(**book_data)
        return super().form_valid(form)
