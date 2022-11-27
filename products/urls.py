from django.urls import path
from products.views import ProductDetailView

urlpatterns = [
    path('<slug:slug>', ProductDetailView.as_view(), name='product'),
    
    
]