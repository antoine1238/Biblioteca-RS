#Django
from django.urls import path
from django.contrib.auth.decorators import login_required

#Views
from .views import *

urlpatterns = [
    path('create/', login_required(BookCreateView.as_view()), name='create_book'),
    path('delete/<slug:slug>/', login_required(BookDeleteView.as_view()), name='delete_book'),
    path('edit/<slug:slug>/', login_required(BookUpdateView.as_view()), name='edit_book'),
    path('<slug:slug>/', BookDetailView.as_view(), name='detail_book'),
]