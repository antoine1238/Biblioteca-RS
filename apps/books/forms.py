#Django
from django import forms

#Models
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {"title","category","synopsis","photo"}
        labels = {
            "title": "Title of the book",
            "category": "Category of the book",
            "synopsis": "book synopsis",
            "photo": "book cover",
        }