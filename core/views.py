#Django
from django.shortcuts import render, redirect
from django.views.generic import View

#Models
from apps.books.models import Book, Category, Review
from apps.author.models import Author

class Home(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        author = Author.objects.filter(id=request.user.id).first()   
        
        if author:
            ids = author.users_who_follow_ids()
            books = Book.objects.filter(author__in=ids) 

        context = {
            "books": Book.objects.all(),
            "categories": Category.objects.all(),
            "books_follow": books
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        busqueda = request.POST["search"]
        context = {
            "books": Book.objects.filter(title__icontains = busqueda),
            "categories": Category.objects.all(),
        }   
        return render(request, self.template_name, context)



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