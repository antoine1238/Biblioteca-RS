#Django
from django import forms

#Models
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {"author", "author_book","title","category","synopsis","photo", "file"}
        labels = {
            "title": "Title of the book",
            "category": "Category of the book",
            "synopsis": "Book synopsis",
            "photo": "Book cover",
            "file": "File pdf",
        }
        widgets = { 
            'author': forms.TextInput(attrs={'class':'hidden', "name":"author"}),
            'title': forms.TextInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"title", "placeholder": "Titulo..."}),
            'author_book': forms.TextInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"author_book", "placeholder": "nombre del autor del libro..."}),
            'synopsis': forms.Textarea(attrs={'class':'w-4/5 h-20 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"synopsis", "placeholder": "Sinopsis..."}),
            'categoria_id': forms.Select(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"category"}),
            'photo': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'photo' }),
            'file': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'file' }),
        }

class BookEditForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = {"author_book","title","synopsis","photo", "file"}
        labels = {
            "title": "Title of the book",
            "synopsis": "Book synopsis",
            "photo": "Book cover",
            "file": "File pdf",
        }
        widgets = { 
            'title': forms.TextInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"title", "placeholder": "Titulo..."}),
            'author_book': forms.TextInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"author_book", "placeholder": "nombre del autor del libro..."}),
            'synopsis': forms.Textarea(attrs={'class':'w-4/5 h-20 mx-auto my-1 p-2 rounded-lg shadow-md lg:w-3/5', "name":"synopsis", "placeholder": "Sinopsis..."}),
            'photo': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'photo' }),
            'file': forms.FileInput(attrs={'class':'w-4/5 mx-auto my-1 p-2 bg-red-100 border-2 border-dashed border-gray-500  shadow-md lg:w-3/5', 'name': 'file' }),
        }
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = {"message", "title", "book", "author"}
        widgets = {
            "message": forms.Textarea(attrs={"class":"border-b border-gray-400 h-28 w-full shadow-lg p-2 rounded-lg hover:bg-gray-100", "name":"message", "placeholder":"reseña..."}),
            "title": forms.TextInput(attrs={"class":"border-b border-gray-400 h-10 w-full shadow-lg p-2 rounded-lg hover:bg-gray-100", "name":"title", "placeholder":"titulo... (opcional)"})
        }

class StarForm(forms.ModelForm):
    class Meta:
        model = Star
        fields = {"author", "book", "stars"}
        widgets = {
            "stars": forms.Select(attrs={"class":"border-b border-gray-400 w-full p-2 rounded-lg hover:bg-gray-100 shadow-lg", "name":"stars"})
        }