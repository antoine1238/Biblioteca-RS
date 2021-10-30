from django.db import models


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
    autor = models.ForeignKey("author.Author", models.SET_NULL, blank=True, null=True,)
    category = models.ManyToManyField(Category)
    synopsis = models.CharField(max_length=255, null=True, blank=True)
    photo = models.ImageField("Photo of the book", upload_to="books_img", null=True, blank=True)
    publication_date = models.DateField(auto_now_add=True)

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return self.title


class Review(models.Model):
    " Each book will have reviews that will be shown in the details of the book. in addition to a score based on 5 stars to determine the value. "
    STARS = (
        ("1", "one star"),
        ("2", "Two stars"),
        ("3", "Three stars"),
        ("4", "Four stars"),
        ("5", "Five stars"),
    )
    message = models.TextField("Review of the autor", null=False, blank=False)
    stars = models.CharField(max_length=1, choices=STARS, null=False, blank=False)
    autor = models.ForeignKey("author.Author", on_delete=models.CASCADE)  
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return f"{self.autor} / {self.book}"

    