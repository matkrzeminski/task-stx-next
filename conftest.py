from datetime import datetime

import pytest

from books.tests.factories import BookFactory


@pytest.fixture()
def book():
    return BookFactory()


@pytest.fixture()
def book_data():
    return {
        "title": "A Beginners Guide to Python 3 Programming",
        "author": "John Hunt",
        "published_date": datetime(2019, 8, 8),
        "isbn": "9783030202903",
        "pages": 433,
        "cover": "http://books.google.com/books/content?id=lEuoDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl"
        "&source=gbs_api",
        "language": "en",
    }
