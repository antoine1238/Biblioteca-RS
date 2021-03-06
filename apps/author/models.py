#Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Models
from django.db import models

# py
import os

#models 
from apps.books.models import Book

# vars
COUNTRIES = (
        ("VEN", "Venezolano/a"),
        ("ESP", "Español/a"),
        ("POR", "Portugues/a"),
        ("COL", "Colombiano/a"),
        ("PER", "Peruano/a"),
        ("MEX", "Mexicano/a"),
        ("CHI", "Chileno/a"),
        ("ARG", "Argentino/a"),
        ("000", "Otro"),
    )
SEX = (
    ("HOM", "Hombre"),
    ("MUJ", "Mujer"),
    ("PLA", "Plátano"),
    ("000", "Otro"),
)

class AuthorManager(BaseUserManager):

    def create_user(self, username, first_name, password, email):
        """ We only fill in the required fields, since the author in his profile has the option to add more information. """
        author = self.model(
            username = username,
            first_name = first_name,
            password = password,
            email = self.normalize_email(email)
        )        
        author.set_password(password)   # Encript password
        author.save()
        print("usuario creado")
        return author

    def create_superuser(self, username, first_name, password, email):
        """ the difference is that here we assign the author the admin permission. """
        author = self.create_user(
            username = username,
            first_name = first_name,
            password = password,
            email = self.normalize_email(email)
        )
        author.is_admin = True
        author.save()
        print("superusuario creado")
        return author


class Author(AbstractBaseUser):
    """Model definition for Autor."""
    username = models.CharField("Username", unique=True, max_length = 100)
    email = models.EmailField("Email", unique=True, max_length = 100, blank=False, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)

    # optional
    photo = models.ImageField("Photo of the author", upload_to="authors_img", null=True, blank=True)
    background_photo = models.ImageField("background photo of the profile author", upload_to="authors_back_img", null=True, blank=True)
    description = models.CharField("Author's description", max_length=255, null=True, blank=True)
    big_description = models.TextField("big description", null=True, blank=True)
    nationality = models.CharField("Author's nationality", max_length=3, choices=COUNTRIES, null=True, blank=True)
    sex = models.CharField("Gender", max_length=3, choices=SEX, null=True, blank=True)

    # social media links
    facebook = models.URLField("facebook link", null=True, blank=True)
    twiter = models.URLField("facebook link", null=True, blank=True)
    instagram = models.URLField("facebook link", null=True, blank=True)
    github = models.URLField("facebook link", null=True, blank=True)

    # automatic
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = AuthorManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "email"]

    class Meta:
        """Meta definition for Autor."""

        verbose_name = 'Autor'
        verbose_name_plural = 'Autors'

    def __str__(self):
        """Unicode representation of Autor."""
        return self.username 

    def delete(self, *args, **kwargs):
        """ In charge of deleting the file corresponding to the "photo" field.  """
        if self.photo:
            if os.path.isfile(self.photo.path):
                os.remove(self.photo.path)

        if self.background_photo:
            if os.path.isfile(self.background_photo.path):
                os.remove(self.background_photo.path)

        super(Author, self).delete(*args,**kwargs)

    def has_perm(self, perm, obj = None):                     
        return True
            
    def has_module_perms(self, app_label):                
        return True 

    def book_count(self):
        book_count = len(Book.objects.filter(author=self.id))
        return book_count

    def user_followers_count(self):
        user_followers_count = len(Relationship.objects.filter(to_user=self.username))
        return user_followers_count
    
    def users_who_follow_count(self):
        Users_who_follow_count = len(Relationship.objects.filter(from_user=self.username))
        return Users_who_follow_count
    
    def users_who_follow_names(self):
        Users_who_follow = Relationship.objects.filter(from_user=self.username)
        lista = []
        for i in Users_who_follow:
            lista.append(i.to_user)
        return lista
    
    def users_who_follow_ids(self):
        Users_who_follow = Relationship.objects.filter(from_user=self.username)
        lista_names = []
        lista = []
        for i in Users_who_follow:
            lista_names.append(i.to_user)

        for i in lista_names:
            obj = Author.objects.get(username = i)
            lista.append(obj.id)
        return lista

    @property
    def is_staff(self):   
        """to assign the user's permission level"""                                 
        return self.is_admin


class Relationship(models.Model):
    from_user = models.CharField("usuario que sigue", max_length=100, null=False, blank=False)
    to_user = models.CharField("usuario al que siguen", max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.from_user} sigue a {self.to_user}"