#Django
from django.shortcuts import render, redirect
from django.views.generic import View, DetailView
from django.db.models import Q

# Forms
from .forms import *

#Models
from .models import *
from apps.books.models import Book



class AuthorsView(View):
    """It allows to list all the authors and also to make the filters in the search bar using the fields "first_name" and "last_name"
        as a filter. excludes you from the list unless you search for yourself in the search bar.
    """
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
    """ In addition to showing the details of the authors, it also shows the books that have been published. """
    model = Author
    template_name = "author/detail_author.html"
    
    def get(self, request, username, *args, **kwargs):
        """ follow / unfollow system using the Relationships model. to determine whether or not I can follow the author I am visiting. """
        # user var
        now_user = request.user.username 

        # receiving user followers
        user_followers = Relationship.objects.filter(to_user=username)
        
        # follower list
        if user_followers:
            lista = []
            for i in user_followers:
                lista.append(i.from_user)
            
            if now_user in lista:
                acction_input = "Dejar de seguir"
            else:
                acction_input = "Seguir"
        else:
            acction_input = "Seguir"

        context = {
            "acction_input":acction_input,
            "author": self.model.objects.get(username = username),
            "books": Book.objects.filter(author__username = username)
        }
        return render(request, self.template_name, context)


class AuthorCreateView(View):
    """ author creation with password validation """
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
    """ To edit the information (excluding the password) and also with a new field aimed at changing the background image of the profile. """
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
            return redirect("detail_author", username=username) 
        else:
            return render(request, "400.html", {"message":"algo pasó y no se pudo guardar"})
            

# follow sistem
def follow(request, username):
    """ Here depending on the variable "action" determine if I can follow or unfollow an author .. create or delete object. """
    if request.method == "POST":
        now_user = request.user.username
        acction = request.POST["acction"]

        if acction == "Seguir":
            rel = Relationship.objects.create(from_user= now_user, to_user= username)
            rel.save()
            return redirect("detail_author", username=username)

        elif acction == "Dejar de seguir":
            rel = Relationship.objects.get(from_user= now_user, to_user=username)
            rel.delete()
            return redirect("detail_author", username=username)
    else:
        return redirect("detail_author", username=username)

