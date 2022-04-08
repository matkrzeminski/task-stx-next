import urllib.parse
from datetime import datetime

import requests


def import_book_data(keywords, title, author, isbn, language):
    """
    Returns first result of Google Books API search based on params,
    if request or params are invalid returns False.
    """
    url = "https://www.googleapis.com/books/v1/volumes?"
    q = f"{keywords}"

    if title != "":
        q += f"+title:{title}"
    if author != "":
        q += f"+inauthor:{author}"
    if isbn != "":
        q += f"+isbn:{isbn}"

    payload = {"q": q, "langRestrict": language}
    payload_str = urllib.parse.urlencode(payload, safe=":+=")

    response = requests.get(url, params=payload_str)
    if response.status_code == 200 and not response.json()["totalItems"] == 0:
        data = response.json()["items"][0]["volumeInfo"]
        title = data.get("title")
        language = data.get("language")
        pages = data.get("pageCount") if data.get("pageCount") else 0
        author = data.get("authors")[0]
        for identifier in data["industryIdentifiers"]:
            if identifier.get("type") == "ISBN_13":
                isbn = identifier.get("identifier")

        cover = None
        if data.get("imageLinks") is not None:
            cover = data.get("imageLinks").get("thumbnail")

        published_date = data.get("publishedDate").split("-")
        if len(published_date) == 3:
            published_date = datetime(
                int(published_date[0]),
                int(published_date[1]),
                int(published_date[2]),
            )
        elif len(published_date) == 2:
            published_date = datetime(int(published_date[0]), int(published_date[1]), 1)
        else:
            published_date = datetime(int(published_date[0]), 1, 1)

        book_data = {
            "title": title,
            "author": author,
            "published_date": published_date,
            "isbn": isbn,
            "pages": pages,
            "cover": cover,
            "language": language,
        }
        return book_data
    return False
