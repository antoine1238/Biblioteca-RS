from django.contrib import admin

#Models
from .models import *

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Review)