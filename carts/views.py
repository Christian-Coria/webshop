from django.shortcuts import render
from carts.models import Cart
from carts.utils import get_or_create_cart
from products.models import Product
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from carts.models import CartProducts


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

    return render(request, 'carts/cart.html', {
        'cart' : cart
    })


def add(request):
    cart = get_or_create_cart(request)   #obtenemos el carrito 
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #Product.objects.get(pk=request.POST.get('product_id')) #obtenemos el producto
    quantity = request.POST.get('quantity', 1)  #obtenemos la cantidad y definimos un valor por defoult 

    # cart.products.add(product, through_defaults={
    #     'quantity' : quantity
    # }) #agregamos el producto al carrito indicando la cantidad

    cart_product = CartProducts.objects.create(cart=cart, 
                                            product=product,    
                                            quantity=quantity)

    return render(request, 'carts/add.html', { 
        'cart_product' : cart_product,
        'product' : product }
        
        )

def remove(request):
    # get_object_or_404 #esta funcion nos permite obtener un objeto apartir de una excepcion y lanzara el error 404
    cart = get_or_create_cart(request) 
    product = get_object_or_404(Product, pk=request.POST.get('product_id'))
    #product = Product.objects.get(pk=request.POST.get('product_id'))
    
    cart.products.remove(product) #asi obtenemos el carro luego el producto y en esta linea eliminamos la relacion entre ellos

    return redirect('carts:cart')