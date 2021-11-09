#Django
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.db.models import Q

# Forms
from .forms import *

#Models
from .models import Author
from apps.books.models import Book



class AuthorsView(View):
    model = Author
    template_name = "author/list_author.html"

    def get(self, request, *args, **kwargs):
        context = {
            "authors": self.model.objects.exclude(username = request.user.username)
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        busqueda = request.POST["search"]
        if busqueda:
            context ={
                "authors": self.model.objects.filter(
                    Q(first_name__icontains = busqueda) |
                    Q(last_name__icontains = busqueda),
                ).distinct()
            } 
            return render(request, self.template_name, context)

        else:
            context = {
                "authors": self.model.objects.exclude(username = request.user.username)
            }
            return render(request, self.template_name, context)



class AuthorDetailView(DetailView):
    model = Author
    template_name = "author/detail_author.html"
    
    def get(self, request, username, *args, **kwargs):
        context = {
            "author": self.model.objects.get(username = username),
            "books": Book.objects.filter(author__username = username)
        }
        return render(request, self.template_name, context)


class AuthorCreateView(View):
    model = Author
    form_class = AuthorForm
    template_name = "author/create_author.html"

    def get(self, request, *args, **kwargs):
        context = {
            "form": AuthorForm
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            """ password validation """
            password_1 = request.POST["password_1"]
            password_2 = request.POST["password_2"]

            if password_1 != password_2:
                context = {
                    "error": "las contraseñas no coinciden",
                    "form": self.form_class
                }
                return render(request, self.template_name, context)
            else:
                form.save()
                return redirect("index")
        else:
            context = {
                "error": "los valores ingresados no son validos",
                "form": self.form_class
            }
            return render(request, self.template_name, context)
            

class AuthorEditView(View):
    model = Author
    form_class = AuthorUpdateForm
    template_name = "author/edit_author.html"

    def get(self, request, username, *args, **kwargs):
        """ If the user does not match the user to edit .. 400.html"""
        user = self.model.objects.get(username=username)
        form = self.form_class(instance = user)

        if username != request.user.username:
            return render(request, "400.html", {"message":"no puedes editar los datos de otro usuario"})

        context = {
            "form": form
        }
        return render(request, self.template_name, context)

    def post(self, request, username, *args, **kwargs):
        user = self.model.objects.get(username=username)
        form = self.form_class(request.POST, request.FILES, instance = user)
        if form.is_valid():
            form.save()
            return redirect("index")
        else:
            return render(request, "400.html", {"message":"algo pasó y no se pudo guardar"})
            