import pytest

from ..utils import import_book_data

pytestmark = pytest.mark.django_db


def test_import_book_data_valid(book_data):
    data = import_book_data("python john hunt", "", "", "", "")
    assert data == book_data

    data = import_book_data("test", "test", "", "", "en")
    assert data["language"] == "en"
    assert "test" in data["title"].lower()

    data = import_book_data("python", "", "", "9783030202903", "")
    assert data["isbn"] == "9783030202903"

    data = import_book_data("python", "", "John Hunt", "", "")
    assert data["author"] == "John Hunt"

    data = import_book_data("Hobbit", "", "", "", "")
    assert "hobbit" in data["title"].lower()


def test_import_book_data_invalid():
    assert not import_book_data("", "", "", "", "")
    assert not import_book_data(
        "big_chunky_test_text_that_should_return_False", "", "", "", ""
    )
