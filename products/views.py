from django.shortcuts import render
from django.views.generic import ListView, DetailView
from products.models import Product
from django.db.models import Q #esta clase nos permite usar diferentes filtros


# Create your views here.
class ProductSearchListView(ListView):
    template_name = 'products/search.html'

    def get_queryset(self):     #este metodo retorna queryset     revisar multiples query
        filters = Q(title__icontains=self.query()) #| Q(category__title__icontains=self.query()) #buscamos por titulo de producto y titulo de categoria
        return Product.objects.filter(filters)

    def query(self):
        return self.request.GET.get('q')   #retornamos el valor recibido en q 
    
    def get_context_data(self, **kwargs): # accedemos a la query para mostrar el context en el html
        context = super().get_context_data(**kwargs)
        context['query'] = self.query()
        context['count'] = context['product_list'].count() #contamos la cantidad de productos 

        return context


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