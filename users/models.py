'''from django.db import models
#from django.contrib.auth.models import User   retiramos la linea ya que trabajamos sobre AbstractUser
from django.contrib.auth.models import AbstractUser

# proximodel es un modelo que hereda de otro y genera no genera una nueva tabla en base de datos solo modifica el comportamiento de la tabla de la que hereda

# sobreescribimos por completo la clase User con AbstractUser o AbstractBaseUser
    AbstractBaseUser:
    id
    password
    last_login

    AbstractUser:
    username
    first_name
    last_name
    email
    password
    groups
    user_permissions
    is_staff
    is_active
    is_superuser
    last_login
    date_joined    '''
'''
class User(AbstractUser):
    # aqui irian los nuevos atributos que un usuario poseeria
    def get_full_name(self):  #en este ejemplo no lo modificamos x lo que solo retornamos los nombres
        return '{} {}'.formar(self.first_name, self.last_name)

def Customer(User):   #es para agregar nuevas funciones a la clase
    class Meta:
        proxy = True  #estas tres lineas hacen que no se genere una nueva tabla

    def get_products(self): #este metodo retorna todos los productos adquiridos por el cliente
        return []


class Profile(models.Model):    #es para agregar nuevos atributos a la clase
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField()

    '''