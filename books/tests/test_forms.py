import pytest

from .factories import BookFactory
from ..forms import BookForm, BookImportForm

pytestmark = pytest.mark.django_db


class TestBookForm:
    def test_clean_isbn(self):
        book = BookFactory.build()
        form_valid = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "pages": book.pages,
                "cover": book.cover,
                "language": book.language,
            }
        )
        assert form_valid.is_valid()
        assert form_valid.clean_isbn() == book.isbn

        form_valid.save()

        form_repeated = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": book.isbn,
                "pages": book.pages,
                "cover": book.cover,
                "language": book.language,
            }
        )

        assert not form_repeated.is_valid()
        assert len(form_repeated.errors) == 1
        assert "isbn" in form_repeated.errors
        assert "ISBN already exists" in form_repeated.errors["isbn"]

        form_invalid = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": "random text",
                "pages": book.pages,
                "cover": book.cover,
                "language": book.language,
            }
        )

        assert not form_invalid.is_valid()
        assert len(form_invalid.errors) == 1
        assert "ISBN must be numeric" in form_invalid.errors["isbn"]

        form_too_short = BookForm(
            {
                "title": book.title,
                "author": book.author,
                "published_date": book.published_date,
                "isbn": 1234,
                "pages": book.pages,
                "cover": book.cover,
                "language": book.language,
            }
        )

        assert not form_too_short.is_valid()
        assert len(form_too_short.errors) == 1
        assert "ISBN must be 13 digits" in form_too_short.errors["isbn"]


class TestBookImportForm:
    def test_clean_isbn(self):
        book = BookFactory.build()
        form_valid = BookImportForm(
            {
                "keywords": book.title,
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "language": book.language,
            }
        )
        assert form_valid.is_valid()
        assert form_valid.clean_isbn() == book.isbn

        form_valid_no_isbn = BookImportForm(
            {
                "keywords": book.title,
                "title": book.title,
                "author": book.author,
                "isbn": "",
                "language": book.language,
            }
        )
        assert form_valid_no_isbn.is_valid()
        assert form_valid_no_isbn.clean_isbn() == ""

        book2 = BookFactory()

        form_repeated = BookImportForm(
            {
                "keywords": book.title,
                "title": book.title,
                "author": book.author,
                "isbn": book2.isbn,
                "language": book.language,
            }
        )

        assert not form_repeated.is_valid()
        assert len(form_repeated.errors) == 1
        assert "isbn" in form_repeated.errors
        assert "ISBN already exists" in form_repeated.errors["isbn"]

        form_invalid = BookImportForm(
            {
                "keywords": book.title,
                "title": book.title,
                "author": book.author,
                "isbn": "random text",
                "language": book.language,
            }
        )

        assert not form_invalid.is_valid()
        assert len(form_invalid.errors) == 1
        assert "ISBN must be numeric" in form_invalid.errors["isbn"]

        form_too_short = BookImportForm(
            {
                "keywords": book.title,
                "title": book.title,
                "author": book.author,
                "isbn": 1234,
                "language": book.language,
            }
        )

        assert not form_too_short.is_valid()
        assert len(form_too_short.errors) == 1
        assert "ISBN must be 13 digits" in form_too_short.errors["isbn"]
