#Django 
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy

#Forms
from .forms import *

#Models 
from .models import *



class BookDetailView(DetailView):
    model = Book
    template_name = "book/detail_book.html"

    def get(self, request, slug, *args, **kargs):
        context = {"book": self.model.objects.get(slug=slug)}
        return render(request, self.template_name, context)

    

class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = "book/create_book.html"

    
    def get_context_data(self, **kwargs):
        context = {
            "categories": Category.objects.all(),
            "form": self.form_class
        }
        return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            author = int(request.POST["author"])
            form.author = author
            
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



    
class BookDeleteView(DeleteView):
    template_name = "book/book_confirm_delete.html"
    model = Book
    success_url = reverse_lazy("index")

    