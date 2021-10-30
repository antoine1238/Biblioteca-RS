#Django
from django.shortcuts import render
from django.views.generic import View

#Models
from .models import Author


class Home(View):

    def get(self, request, *args, **kwargs):
        context = {
            "authors": Author.objects.all()
        }
        return render(request, "index.html", context)