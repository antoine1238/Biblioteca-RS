#Django
from django import forms

#Models
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {"title","category","synopsis","photo", "file"}
        labels = {
            "title": "Title of the book",
            "category": "Category of the book",
            "synopsis": "Book synopsis",
            "photo": "Book cover",
            "file": "File pdf",
        }
        widgets = { 
            'title': forms.TextInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"title", "placeholder": "Titulo..."}),
            'synopsis': forms.Textarea(attrs={'class':'w-4/5 h-20 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"synopsis", "placeholder": "Sinopsis..."}),
            'categoria_id': forms.Select(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"category"}),
            'photo': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'photo' }),
            'file': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'file' }),
        }