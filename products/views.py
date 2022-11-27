from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product

# Create your views here.

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs): # este metodo se encarga de pasar el contexto de la clase al template

        context = super().get_context_data(**kwargs) # obtenemos el context de la clase padre
        context['message'] = 'Listado de Productos'
        context['products'] = context['product_list']
      
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'