from django.http import HttpResponse
from second_hw_app.models import Product, Client #,Order


def get_clients(request):
    clients = Client.objects.all()
    res = '<br>'.join([str(client) for client in clients])
    return HttpResponse(res)


def get_products(request):
    products = Product.objects.all()
    res = '<br>'.join([str(product) for product in products])
    return HttpResponse(res)
