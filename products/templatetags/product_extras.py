from django import template

register = template.Library()

#aqui definimos las funciones a implementar como filters

@register.filter
def price_format(value):
    return '${0:.2f}'.format(value)