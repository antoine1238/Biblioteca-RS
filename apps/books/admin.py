from django.contrib import admin

#Models
from .models import *

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', "publication_date")
    prepopulated_fields = {'slug': ('title',)} # auto rellenado

admin.site.register(Category)
admin.site.register(Book, BookAdmin)
admin.site.register(Review)
admin.site.register(Star)