import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains, assertNotContains

from books.tests.factories import BookFactory

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
    assertContains(response, "Date Published")


def test_book_add_view(client):
    title = "Test Book"
    author = "Test Author"
    published_date = "2020-01-01"
    isbn = "123456789"
    pages = 100
    language = "en"
    request_data = {
        "title": title,
        "author": author,
        "published_date": published_date,
        "isbn": isbn,
        "pages": pages,
        "language": language
    }
    url = reverse("books:create")
    response = client.post(url, request_data)
    assertContains(response, title)
    assertContains(response, author)
    assertContains(response, published_date)
    assertContains(response, isbn)
    assertContains(response, pages)
    assertContains(response, language)


def test_book_add_view_book_already_exists(client, book):
    url = reverse("books:create")
    request_data = {
        "title": book.title,
        "author": book.author,
        "published_date": book.published_date,
        "isbn": book.isbn,
        "pages": book.pages,
        "language": book.language
    }
    response = client.post(url, request_data)
    assertContains(response, "ISBN already exists")


def test_book_update_view(client, book):
    url = reverse("books:update", kwargs={"pk": book.pk})
    response = client.get(url)
    assertContains(response, book.title)
    assertContains(response, book.author)
    assertContains(response, book.published_date)
    assertContains(response, book.isbn)
    assertContains(response, book.pages)
    assertContains(response, book.language)

    request_data = {
        "title": "Test Book",
        "author": "Test Author",
        "published_date": "2020-01-01",
        "isbn": "123456789",
        "pages": 100,
        "language": "en"
    }
    response = client.post(url, request_data)
    assertContains(response, "Test Book")
    assertContains(response, "Test Author")
    assertContains(response, "2020-01-01")
    assertContains(response, "123456789")
    assertContains(response, 100)
    assertContains(response, "en")


def test_book_update_view_book_already_exists(client, book):
    url = reverse("books:update", kwargs={"pk": book.pk})
    book2 = BookFactory()
    request_data = {
        "title": "Test Book",
        "author": "Test Author",
        "published_date": "2020-01-01",
        "isbn": book2.isbn,
        "pages": 100,
        "language": "en"
    }
    response = client.post(url, request_data)
    assertContains(response, "ISBN already exists")


def test_book_delete_view(client, book):
    url = reverse("books:delete", kwargs={"pk": book.pk})
    response = client.get(url)
    assertContains(response, book.title)
    assertContains(response, book.author)
    assertContains(response, "Are you sure you want to delete this book?")

    response = client.post(url)
    assert response.status_code == 302
    assert response.url == reverse("books:filter")

    url = response.url
    response = client.get(url)
    assertNotContains(response, book.title)
    assertNotContains(response, book.author)
    assertNotContains(response, book.published_date)
    assertNotContains(response, book.isbn)
    assertNotContains(response, book.pages)
    assertNotContains(response, book.language)
