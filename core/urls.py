#Django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

#Views
from .views import Home, category_filter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('categoria/<str:name>', category_filter, name='category_filter'),

    path('author/', include("apps.author.urls"), name="author"),
    path('books/', include("apps.books.urls"), name="books"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



