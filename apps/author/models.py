#Django
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

#Models
from django.db import models


class AuthorManager(BaseUserManager):

    def create_user(self, username, first_name, password, email):
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
    COUNTRIES = (
        ("VEN", "Venezolano"),
        ("ESP", "Español"),
        ("COL", "Colombiano"),
        ("PER", "Peruano"),
    )
    
    SEX = (
        ("MAN", "Man"),
        ("WOM", "Woman"),
        ("???", "???"),
    )

    username = models.CharField("Username", unique=True, max_length = 100)
    email = models.EmailField("Email", unique=True, max_length = 100, blank=False, null=False)
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField("Photo of the author", upload_to="authors_img", null=True, blank=True)
    description = models.CharField("Author's description", max_length=255, null=True, blank=True)
    nationality = models.CharField("Author's nationality", max_length=3, choices=COUNTRIES, null=True, blank=True)
    sex = models.CharField("Gender", max_length=3, choices=SEX, null=True, blank=True)
    is_admin = models.BooleanField(default=False)

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

    def has_perm(self, perm, obj = None):                     
        return True
            
    def has_module_perms(self, app_label):                
        return True

    @property
    def is_staff(self):   
        """to assign the user's permission level"""                                 
        return self.is_admin
