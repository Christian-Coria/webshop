from django.db import models
#from users.models import User
from products.models import Product
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
import uuid
from django.db.models.signals import m2m_changed
import decimal


class Cart(models.Model):
    cart_id = models.CharField(max_length=100, null=False,blank=False, unique=True)
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='CartProducts') #hacemos la relacion que nos permitira sumar cantidad de productos
    subtotal =models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    total =models.DecimalField(default=0.0, max_digits=8, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    #FEE es una comision
    FEE = 0.3 # en este caso del 30%

    def __str__(self):
        return self.cart_id

    def update_totals(self):
        self.update_subtotal()
        self.update_total()

    def update_subtotal(self):
        
        self.subtotal = sum([
            cp.quantity * cp.product.price for cp in self.products_related()
        ]) # la suma del precio del producto por la cantidad y luego las suma de la lista
        #  
        #sum([product.price for product in self.products.all()])==> es la suma del precio de todos los productos
        self.save()

    def update_total(self): #es el sub + comision y convertimos el FEE en un decimal
        self.total = self.subtotal + (self.subtotal * decimal.Decimal(Cart.FEE))
        self.save()


def set_cart_id(sender, instance, *args, **kwargs):
    if not instance.cart_id:
        instance.cart_id = str(uuid.uuid4())
        

def update_totals(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or 'post_remove' or 'post_clear': # osea despues de que un carrito se crea o borra o se limpia
        instance.update_totals() #se calcula el subtotal y el total del carrito

def post_save_update_totals(sender, instance, *args, **kqargs):         # es el nuevo callback ya no update_callback
        instance.cart.update_totals #osea nuestro obj cartsproducts,y el metodo declarado en la funcion mas arriba ==> asi nos daria el subtotal

def products_related(self): #obtenemos en una misma consulta 
    return self.cartproducts_set.select_related('product') #todos los objetos cartproduct y product

class CartProducts(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)     # en las primeras 2 lineas definimos la relacion
    quantity = models.IntegerField(default=1)   #definimos cuanto de un producto se agregara al carito
    created_at = models.DateTimeField(auto_now_add=True)



pre_save.connect(set_cart_id, sender=Cart)
post_save.connect(post_save_update_totals, sender=CartProducts)
m2m_changed.connect(update_totals, sender=Cart.products.through)#registramos el callback