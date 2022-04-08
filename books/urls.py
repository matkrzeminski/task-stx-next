from django.urls import path

from books.views import (
    BookUpdateView,
    BookCreateView,
    BookImportView,
    BookListAPIView,
    BookFilterView,
    BookDeleteView,
)

urlpatterns = [
    path("", BookFilterView.as_view(), name="filter"),
    path("api/", BookListAPIView.as_view(), name="api"),
    path("import/", BookImportView.as_view(), name="import"),
    path("add/", BookCreateView.as_view(), name="create"),
    path("<int:pk>/update/", BookUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", BookDeleteView.as_view(), name="delete"),
]
