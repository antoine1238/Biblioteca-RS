#Django
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

#Views
from apps.author.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='home'),

    path('author/', include("apps.author.urls"), name="author"),
    path('books/', include("apps.books.urls"), name="books"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



