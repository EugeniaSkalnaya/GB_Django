from django.urls import path
from .views import get_clients,get_products, show_order

urlpatterns = [
    path('clients/', get_clients, name='clients'),
    path('products/', get_products, name='products'),
    path('orders/', show_order, name='orders'),
]