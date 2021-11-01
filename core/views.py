#Django
from django.shortcuts import render, redirect
from django.views.generic import View

#Form
from apps.books.forms import BookForm

#Models
from apps.books.models import Book, Category, Review

class Home(View):
    
    def get_context_data(self, **kwargs):
        context = {
            "books": Book.objects.all(),
            "categories": Category.objects.all(),
        }
        return context

    def get(self, request, *args, **kwargs):
        return render(request, "index.html", self.get_context_data())

    def post(self, request, *args, **kwargs):
        busqueda = request.POST["search"]
        context = {
            "books": Book.objects.filter(title__icontains = busqueda),
            "categories": Category.objects.all(),
        }   
        print(context)     
        return render(request, "index.html", context)


def category_filter(request, name):
    context = {
        "books": Book.objects.filter(category__name__icontains = name),
        "categories": Category.objects.all()
    }
    return render(request, "index.html", context)