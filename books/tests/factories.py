from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Book


class BookFactory(DjangoModelFactory):
    title = Faker("sentence", nb_words=6)
    author = Faker("name")
    published_date = Faker("date")
    isbn = Faker("isbn13", separator="")
    pages = Faker("random_int", min=10, max=10000)
    cover = Faker("image_url")
    language = Faker("language_code")

    class Meta:
        model = Book
        django_get_or_create = ["isbn"]
