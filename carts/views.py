from django.shortcuts import render
from carts.models import Cart
from carts.utils import get_or_create_cart
from products.models import Product


def cart(request):
    '''crear una session:
    request.session['cart_id']= '123' #el atributo session es un diccionario

    para corroborar por terminal la session:
    valor = request.session.get('cart_id')
    print(valor) ---- asi obtenemosel id de la session iniciada 
    
    eliminar la session:
    request.session['cart_id']= None
    
    asi:
    '''
    #request.session['cart_id'] = None #---tuve que eliminar la session existente para que no diera error "doesNotExist car..."

    '''
    if cart_id:#request.session.get('cart_id'): #si la session esta iniciada obtenemos el carrito de la base de datos
        cart = Cart.objects.get(cart_id=cart_id)#=reque(pkst.session.get('cart_id'))
    else: #caso contrario creamos el carrito
        cart = Cart.objects.create(user=user)      -   refactor para evitar error si en el if no se encuentra el carro de compras '''
    #cart = Cart.objects.filter(cart_id=cart_id)  #usamos el metodo filter en vez del get que nos retorna el error si el cart_id no exist

    
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html', {})


def add(request):
    cart = get_or_create_cart(request)   #obtenemos el carrito 
    product = Product.objects.get(pk=request.POST.get('product_id')) #obtenemos el producto

    cart.products.add(product) #agregamos el producto al carrito

    return render(request, 'carts/add.html', { 'product' : product })