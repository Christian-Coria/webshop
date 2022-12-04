from django import forms
from django.contrib.auth.models import User
#from users.models import User -- Cambiamos las referencias al modelo

class RegisterForm(forms.Form):      #Estilos en forms:
    username = forms.CharField(required=True,
                                min_length=4, max_length=20,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id':'username',
                                    'placeholder':'Username'
                                }) )
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={
                                    'class': 'form-control',
                                    'id':'email',
                                    'placeholder':'TuCorreo@mail.com'
                                }) )
    password = forms.CharField(     label='Contraseña',
                                    required=True,widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id':'password',
                                    'placeholder':'Password'
                                }) )
    password2 = forms.CharField(    label='Confirmar Contraseña',
                                    required=True,widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id':'password2',
                                    'placeholder':'Password 2'
                                }) )      # label='....' modificamos asi el texto del label

    def clean_username(self): # clean_username le decimos a django que vamos a generar una validacion en este caso a username
        username = self.cleaned_data.get('username') # asi obtenemos el username del servidor
        if User.objects.filter(username=username).exists(): # ahora consultamos a la BD si el user existe o no (importamos el modelo User)
            raise forms.ValidationError('El Username ya esta en Uso') #retornamos el error (admas hay que validar el mje en el html)

            return username #caso contrario retornamos el user 

    def clean_email(self): 
        email = self.cleaned_data.get('email') 
        if User.objects.filter(email=email).exists(): 
            raise forms.ValidationError('El Email ya esta en Uso') 

            return email #caso contrario
    
    def clean(self): # redefinimos el metodo clean cuando un campo dependa de otro (que ambas contraseñas sean iguales)
        cleaned_data = super().clean() #obtenemos todos los campos del formulario 
        
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La Contraseña no Coincide!' ) #el primer parametro es el campo que se va a validar ...
            
    def save(self): # este metodo se encarga de persistir y clrear un nuevo usuario    
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
        )    
