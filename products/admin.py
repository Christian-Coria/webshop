from django.contrib import admin
from products.models import Product

class ProductAdmin(admin.ModelAdmin): #modificamos el comportamiento de la clase en el admin
    fields = ('title', 'description', 'price')
    list_display = ('__str__', 'slug','created_at')


admin.site.register(Product, ProductAdmin)
# Register your models here.
