import pytest

pytestmark = pytest.mark.django_db


def test_book__str__(book):
    string = f"{book.title} by {book.author}"
    assert book.__str__() == string
    assert str(book) == string
