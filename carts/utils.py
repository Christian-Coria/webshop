from carts.models import Cart


def get_or_create_cart(request):
    user = request.user if request.user.is_authenticated else None # si esta autenticado obtenemos caso contrario creamos
    cart_id = request.session.get('cart_id')    # asi intentamos obtener el cart_id
    cart = Cart.objects.filter(cart_id=cart_id).first() # asi intentamos obtener el carrito

    if cart is None:
        cart = Cart.objects.create(user=user) #si el carrito no existe lo creamos desde la session
    if user and cart.user is None:   #si el user existe, y esta autenticado y el carrito en su atributo user is none asignamos el user al carrito
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id # la session almacena el id del carrito creado

    return cart