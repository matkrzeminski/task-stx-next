import pytest
from django.urls import reverse, resolve

pytestmark = pytest.mark.django_db


def test_filter_reverse():
    """books:filter should reverse to '/'."""
    assert reverse("books:filter") == "/"


def test_filter_resolve():
    """'/' should resolve to books:filter."""
    assert resolve("/").view_name == "books:filter"


def test_api_reverse():
    """books:api should reverse to '/api/'."""
    assert reverse("books:api") == "/api/"


def test_api_resolve():
    """'/api/' should resolve to books:api."""
    assert resolve("/api/").view_name == "books:api"


def test_import_reverse():
    """books:import should reverse to '/import/'."""
    assert reverse("books:import") == "/import/"


def test_import_resolve():
    """'/import/' should resolve to books:import."""
    assert resolve("/import/").view_name == "books:import"


def test_add_reverse():
    """books:create should reverse to '/add/'."""
    assert reverse("books:create") == "/add/"


def test_add_resolve():
    """'/add/' should resolve to books:create."""
    assert resolve("/add/").view_name == "books:create"


def test_update_reverse(book):
    """books:update should reverse to '/<pk>/update/'."""
    assert reverse("books:update", kwargs={"pk": book.pk}) == f"/{book.pk}/update/"


def test_update_resolve(book):
    """'/<pk>/update/' should resolve to books:update."""
    assert resolve(f"/{book.pk}/update/").view_name == "books:update"


def test_delete_reverse(book):
    """books:delete should reverse to '/<pk>/delete/'."""
    assert reverse("books:delete", kwargs={"pk": book.pk}) == f"/{book.pk}/delete/"


def test_delete_resolve(book):
    """'/<pk>/delete/' should resolve to books:delete."""
    assert resolve(f"/{book.pk}/delete/").view_name == "books:delete"
