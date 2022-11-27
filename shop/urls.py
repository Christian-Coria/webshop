from django.urls import path
from shop.views import index, login_view, logout, registro
from products.views import ProductListView
urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('login/', login_view, name='login'),
    path('logout/', login_view, name='logout'),
    path('registro/', registro, name='registro'),
]