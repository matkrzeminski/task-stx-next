import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

pytestmark = pytest.mark.django_db


def test_book_import_view_form_valid(client, book):
    url = reverse("books:import")

    request_data = {
        "keywords": "test",
        "title": "",
        "author": "",
        "isbn": "",
        "language": "",
    }
    response = client.post(url, request_data)
    assert response.status_code == 302
    assert response.url == reverse("books:filter")

    request_data = {
        "keywords": "big_chunky_test_text_that_should_return_False",
        "title": "",
        "author": "",
        "isbn": "",
        "language": "",
    }
    response = client.post(url, request_data)
    assertContains(response, "No books found.")


def test_book_filter_view(client):
    url = reverse("books:filter")
    response = client.get(url)
    assertContains(response, "Title")
    assertContains(response, "Author")
    assertContains(response, "Language Code")
