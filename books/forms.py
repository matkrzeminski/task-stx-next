from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from books.models import Book


class BookImportForm(forms.Form):
    keywords = forms.CharField(max_length=255, required=True)
    title = forms.CharField(max_length=255, required=False)
    author = forms.CharField(max_length=255, required=False)
    isbn = forms.CharField(max_length=13, required=False)
    language = forms.CharField(label="Language Code", max_length=2, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("keywords", css_class="form-group col-md-6 mb-0"),
                Column("title", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("author", css_class="form-group col-md-4 mb-0"),
                Column("isbn", css_class="form-group col-md-4 " "mb-0"),
                Column("language", css_class="form-group col-md-4 mb-0"),
            ),
            Submit("submit", "Import", css_class="float-end"),
        )

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        if isbn == "":
            return isbn
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must be numeric", code="not_a_number")
        if len(str(isbn)) != 13:
            raise forms.ValidationError("ISBN must be 13 digits", code="too_short")
        try:
            Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            return isbn
        raise forms.ValidationError("ISBN already exists", code="isbn_exists")


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column("title", css_class="form-group col-md-6 mb-0"),
                Column("author", css_class="form-group col-md-6 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("published_date", css_class="form-group col-md-4 mb-0"),
                Column("isbn", css_class="form-group col-md-4 mb-0"),
                Column("pages", css_class="form-group col-md-4 mb-0"),
                css_class="form-row",
            ),
            Row(
                Column("cover", css_class="form-group col-md-6 mb-0"),
                Column("language", css_class="form-group " "col-md-6 mb-0"),
                css_class="form-row",
            ),
            Submit("submit", "Submit", css_class="float-end"),
        )

    def clean_isbn(self):
        isbn = self.cleaned_data["isbn"]
        if not isbn.isdigit():
            raise forms.ValidationError("ISBN must be numeric", code="not_a_number")
        if len(str(isbn)) != 13:
            raise forms.ValidationError("ISBN must be 13 digits", code="too_short")
        try:
            Book.objects.get(isbn=isbn)
        except Book.DoesNotExist:
            return isbn
        raise forms.ValidationError("ISBN already exists", code="isbn_exists")
