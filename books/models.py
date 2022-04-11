from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField("Date Published (YYYY-MM-DD)")
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.IntegerField("Number of Pages")
    cover = models.URLField(
        "Cover url",
        blank=True,
        null=True,
    )
    language = models.CharField("Publication Language Code", max_length=2)

    class Meta:
        ordering = ("-published_date",)

    def __str__(self):
        return f"{self.title} by {self.author}"
