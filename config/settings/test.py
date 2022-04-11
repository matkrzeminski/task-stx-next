from .base import *
from .base import env

SECERET_KEY = env(
    "SECRET_KEY",
    default="77c6WEgznSNmOtTbFMifgkw7lJtFxQvI8iJsnyYqgpS_EnOJ7caRApEkp1gGHlsy",
)

TEST_RUNNER = "django.test.runner.DiscoverRunner"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}
