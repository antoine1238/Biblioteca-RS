#Django
from django.shortcuts import render
from django.views.generic import View

#Form
from .forms import *

#Models
from .models import *

class HomeBookView(View):

    def get(self, request, *args, **kwargs):
        context = {
            "books": Book.objects.all(),
            "categorys": Category.objects.all(),
            "reviews": Review.objects.all(),
            "form": BookForm
        }
        return render(request, "books.html", context)