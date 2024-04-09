from django.urls import path
from .views import get_clients, get_products, order, get_client, \
    client_order_products, get_orders, get_order, upload_image

urlpatterns = [
    path('clients/', get_clients, name='clients'),
    path('clients/<int:pk>/', get_client, name='get_client'),
    path('products/', get_products, name='products'),
    path('clients/<int:pk>/orders/', order, name='order'),
    path('clients/<int:pk>/orders/<int:days>/', client_order_products, name='client_order_products'),
    path("orders/", get_orders, name="get_orders"),
    path("orders/<int:pk>/", get_order, name="get_order"),
    path('upload/', upload_image, name='upload_image'),
]
