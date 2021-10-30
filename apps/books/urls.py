from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('list/', HomeBookView.as_view(), name='list'),
]