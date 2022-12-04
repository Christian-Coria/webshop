from django.urls import path
from carts.views import cart, add

app_name = 'carts'

urlpatterns = [
    path('', cart, name='cart'),
    path('agregar/', add, name='add')
    
]