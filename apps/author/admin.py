from django.contrib import admin


#Models
from .models import *


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", 'username')


admin.site.register(Author, AuthorAdmin)