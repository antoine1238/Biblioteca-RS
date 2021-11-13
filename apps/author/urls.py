# Django
from django.urls import path

#Views
from .views import *

urlpatterns = [
    path('list/', AuthorsView.as_view(), name='list_author'),
    path('create/', AuthorCreateView.as_view(), name='create_author'),
    path('edit/<str:username>', AuthorEditView.as_view(), name='edit_author'),
    path('detail/<str:username>/', AuthorDetailView.as_view(), name='detail_author'),
    path('follow/<str:username>/', follow, name='follow'),
]