#Django
from django.db import models

# py
import os

class Category(models.Model):
    """ Categories of books, to order them. """
    name = models.CharField("name of category", max_length=20, null=False, blank=False)

    class Meta:
        """Meta definition for CategoryBlog."""
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Book(models.Model):
    """Model definition for Book."""
    title = models.CharField("Title of the book", max_length=80, unique=True, null=False, blank=False)
    author = models.ForeignKey("author.Author", models.SET_NULL, blank=True, null=True,)
    author_book = models.CharField("author of the book", max_length=80, null=False, blank=False)
    category = models.ManyToManyField(Category) 
    synopsis = models.TextField(null=False, blank=False)
    photo = models.ImageField("Photo of the book", upload_to="books_img", null=False, blank=False)
    file = models.FileField("File of the book", upload_to="books_pdf", null=False, blank=False)
    publication_date = models.DateField(auto_now_add=True)

    # automatically
    short_synopsis = models.CharField(max_length=255, null=True, blank=True) # se rellenará automaticamente en base al "synopsis" field
    slug = models.SlugField(null=True, unique=True)
    
    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return f"{self.title}, {self.author_book}"

    def get_absolute_url(self): 
        """its value is the model slug"""
        from django.urls import reverse
        return reverse('detail_book', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): 
        """ To save the slug and short_synopsis automatically.""" 
        self.short_synopsis = self.synopsis[:255]
        if not self.slug:
            self.slug = self.title.replace(" ", "-")
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """ In charge of deleting the files corresponding to the "file" and "photo" fields.  """
        if os.path.isfile(self.file.path):
            os.remove(self.file.path)

        if os.path.isfile(self.photo.path):
            os.remove(self.photo.path)
            
        super(Book, self).delete(*args, **kwargs)

class Review(models.Model):
    " Each book will have reviews that will be shown in the details of the book. "
    message = models.TextField("Review of the autor", null=False, blank=False)
    author = models.ForeignKey("author.Author", on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.author} / {self.book}"

    
class Star(models.Model):
    """ stars that will rate the quality of the book. """
    STARS = (
        ("1", "one star"),
        ("2", "Two stars"),
        ("3", "Three stars"),
        ("4", "Four stars"),
        ("5", "Five stars"),
    )
    stars = models.CharField(max_length=1, choices=STARS, null=False, blank=False)
    author = models.ForeignKey("author.Author", on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Star'
        verbose_name_plural = 'Stars'

    def __str__(self):
        return f"{self.book}-{self.author} <{self.stars} stars>"
