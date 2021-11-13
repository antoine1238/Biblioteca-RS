#Django 
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

#Forms
from .forms import *

#Models 
from .models import *



class BookDetailView(DetailView):
    """renders the content of the book, and allows to create the reviews of other authors"""
    model = Book
    form_class = ReviewForm
    template_name = "book/detail_book.html"

    def get(self, request, slug, *args, **kargs):
        context = {
            "review_form": self.form_class,
            "book": self.model.objects.get(slug=slug),
            "reviewer": Review.objects.filter(book = self.model.objects.get(slug=slug)).order_by("-date")
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("detail_book", slug=slug)

    

class BookCreateView(CreateView):
    """ Creation of books and also does not allow uploading to the "file" field files that are not type PDF. """
    model = Book
    form_class = BookForm
    template_name = "book/create_book.html"
    
    def get_context_data(self, **kwargs):
        context = {
            "form": self.form_class
        }
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            name_file = str(form.cleaned_data["file"])
            if not name_file.endswith('.pdf'):
                context = {
                    "categories": Category.objects.all(),
                    "form": self.form_class,
                    "error": "No has ingresado un archivo PDF"
                }
                return render(request, self.template_name, context)
            else:
                form.save()
                return redirect("index")
        else:
            return render(request, self.template_name, self.get_context_data())


class BookUpdateView(View):
    """ To update the data of the book, like create, this does not allow uploading files that are not type pdf. """
    model = Book
    form_class = BookEditForm
    template_name = "book/edit_book.html"

    def get(self, request, slug, *args, **kwargs):
        book = Book.objects.get(slug=slug)
        context = {
            "book": book,
            "form":self.form_class(instance=book)
        }
        return render(request, self.template_name, context)

    def post(self, request, slug, *args, **kwargs):
        book = Book.objects.get(slug=slug)
        form = self.form_class(request.POST, request.FILES, instance=book)
        if form.is_valid():
            name_file = str(form.cleaned_data["file"])
            if not name_file.endswith('.pdf'):
                context = {
                    "book": book,
                    "form": self.form_class(instance=book),
                    "error": "No has ingresado un archivo PDF"
                }
                return render(request, self.template_name, context)
            else:
                form.save()
                return redirect("detail_book", slug=slug)
        else:
            context = {
                "book": book,
                "form": self.form_class(instance=book),
                "error": "No has ingresado datos validos"
            }
            return render(request, self.template_name, context)

    
class BookDeleteView(DeleteView):
    """ Simple removal """
    model = Book
    template_name = "book/book_confirm_delete.html"
    success_url = reverse_lazy("index")


def review_delete(request, id):
    """ Deletion and redirection to the book detail where I was using the book slug. """
    review = Review.objects.get(id=id)
    book = Book.objects.get(id=review.book.id)
    review.delete()
    return redirect("detail_book", slug=book.slug)


class ReviewUpdateView(View):
    """ To be able to modify the reviews published in the details of the corresponding book. """
    model = Review
    form_class = ReviewForm

    def post(self, request, id, slug, *args, **kwargs):
        review = self.model.objects.get(id = id)
        form = self.form_class(request.POST, instance = review)
        if form.is_valid():
            form.save()
            return redirect("detail_book", slug=slug)