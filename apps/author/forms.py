# Django
from django import forms

# Models
from .models import Author

class AuthorForm(forms.ModelForm):
    password_1 = forms.CharField(label = "Contraseña", widget = forms.PasswordInput(
        attrs = {
            "placeholder": "contraseña",
            "id": "password_1",
            "required": "required",
            'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 

        }
    ))
    password_2 = forms.CharField(label = "Confirmación de Contraseña", widget = forms.PasswordInput(
        attrs = {
            "placeholder": "ingrese de nuevo su contraseña",
            "id": "password_2",
            "required": "required",
            'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 

        }
    ))  

    class Meta: 
        model = Author
        fields = ["username", "email", "first_name", "last_name", "photo", "description", "big_description", "nationality", "sex"]
        widgets = { 
            'username': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"username", 
                "placeholder": "elpepe123"}),

            'email': forms.EmailInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"email", 
                "placeholder": "correo@gmail.com"}),

            'first_name': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"first_name", 
                "placeholder": "nombres"}),

            'last_name': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'last_name', 
                "placeholder": "apellidos"}),

            'photo': forms.FileInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'photo'}),
            
            'background_photo': forms.FileInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'background_photo'}),

            'description': forms.TextInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'description', 
                "placeholder": "descripción breve que aparecerá en las tarjetas en las busquedas"}),

            'big_description': forms.Textarea(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white h-20 rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'big_description', 
                "placeholder": "descripción larga ideal para mostrar en tu perfil y dar a conocer mas de tí"}),

            'nationality': forms.Select(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'nationality', 
                "placeholder": "nacionalidad"}),

            'sex': forms.Select(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'sex', 
                "placeholder": "usuario"}),
        }


    def save(self, commit = True):                 
        author = super().save(commit=False)
        author.set_password(self.cleaned_data["password_1"])
        if commit:
            author.save()
        return author    

    
class AuthorUpdateForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["username", "email", "first_name", "last_name", "background_photo", "photo", "description", "big_description", "nationality", "sex",
                    "facebook", "twiter", "instagram", "github"]
        widgets = { 
            'username': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"username", 
                "placeholder": "elpepe123"}),

            'email': forms.EmailInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"email", 
                "placeholder": "correo@gmail.com"}),

            'first_name': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                "name":"first_name", 
                "placeholder": "nombres"}),

            'last_name': forms.TextInput(attrs={
                "required": "required",
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'last_name', 
                "placeholder": "apellidos"}),

            'photo': forms.FileInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'photo'}),
            
            'background_photo': forms.FileInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'background_photo'}),

            'description': forms.TextInput(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'description', 
                "placeholder": "descripción breve que aparecerá en las tarjetas en las busquedas"}),

            'big_description': forms.Textarea(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white h-20 rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'big_description', 
                "placeholder": "descripción larga ideal para mostrar en tu perfil y dar a conocer mas de tí"}),

            'nationality': forms.Select(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'nationality', 
                "placeholder": "nacionalidad"}),

            'sex': forms.Select(attrs={
                'class':'border-0 px-3 py-3 placeholder-blueGray-300 text-blueGray-600 bg-white rounded text-sm shadow focus:outline-none focus:ring w-full ease-linear transition-all duration-150', 
                'name':'sex', 
                "placeholder": "usuario"}),                
        }
