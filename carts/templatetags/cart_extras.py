#aqui se colocan las diferentes funciones que usaremos como filters

#1) registramos la funcion como filters
from django import template

#2) registramos
register = template.Library()


@register.filter
def quantity_product_format(quantity=1):
    return '{} {}'.format(quantity, 'productos' if quantity > 1 else 'producto')

@register.filter
def quantity_add_format(quantity=1) :
    return '{} {}'.format(
        quantity_product_format(quantity),
        'agregados' if quantity > 1 else 'agregado'
    )

    #estas funciones nos permitirian variar entre singular o plusral dependiendo de la cantidad de articulos agregados