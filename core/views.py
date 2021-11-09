#Django
from django.shortcuts import render, redirect
from django.views.generic import View

#Models
from apps.books.models import Book, Category, Review
from apps.author.models import Author

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
        return render(request, "index.html", context)



def category_filter(request, name):

    if request.method == "POST":
        busqueda = request.POST["search"]
        if not busqueda:
            return redirect("index")

        else:
            context = {
                "books": Book.objects.filter(title__icontains = busqueda, category__name=name),
                "categories": Category.objects.all(),
            }   
        return render(request, "index.html", context)

    else:
        context = {
            "books": Book.objects.filter(category__name__icontains = name),
            "categories": Category.objects.all()
        }
        return render(request, "index.html", context)