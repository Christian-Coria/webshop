from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login, logout
from django.contrib import messages
from shop.forms import RegisterForm
from django.contrib.auth.models import User 
from products.models import Product
#from users.models import User #-- Cambiamos las referencias al modelo

def index(request):

    products = Product.objects.all().order_by('-id') #ordenamos la lista de modo descendente

    return render(request,'index.html', { 
            'message': 'Listado de Productos',
            'titulo' : 'Productos',
            'products' : products,
            })
                # {'titulo': 'Modulo A51',' precio': '$15000', 'stock':True},
                # {'titulo': 'Modulo j7 16',' precio': '$9500', 'stock':True},
                # {'titulo': 'Modulo a01',' precio': '$8000', 'stock':False},
         

          
          

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')  # esta validacion es para que el usuario no pueda ingresar desde la barra sin loguearse 
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('index')    
        else:
            messages.error(request, 'Error de Clave o Usuario')

    return render(request, 'account/login.html', {
        
    })

def logout_view(request):


    logout(request)
    messages.success(request, 'Deslogueado Exitosamente')
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('index')  # esta validacion es para que el usuario no pueda ingresar desde la barra sin loguearse 

    form = RegisterForm(request.POST or None) #le decimos que genere un formulario con los datos recibidos o si no se recibe nada vacio (None)

    if request.method == 'POST' and form.is_valid() :                    #concluimos que el formulario envio la informacion y validamos 
        
        user = form.save()
        if user:    # si el usuario se creo mandamos un mensaje
            login(request, user) # iniciamos la sesion
            messages.success(request, 'Creado Exitosamente')
            return redirect('index')   # y redirigimos al index 
        
    return render(request, 'account/registro.html', {
            'form' : form
    })