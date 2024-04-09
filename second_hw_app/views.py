from datetime import timezone
from datetime import timedelta

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from second_hw_app.models import Product, Client, Order

from second_hw_app.forms import ImageForm


def get_clients(request):
    clients = Client.objects.all()
    res = '<br>'.join([str(client) for client in clients])
    return HttpResponse(res)


def get_client(request, pk):
    client = Client.objects.filter(pk=pk)
    return HttpResponse(client)


def get_orders(request):
    orders = Order.objects.all()
    return HttpResponse(orders)


def get_order(request, pk):
    orders = Order.objects.filter(pk=pk)
    return HttpResponse(orders)


def get_products(request):
    products = Product.objects.all()
    res = '<br>'.join([str(product) for product in products])
    return HttpResponse(res)


def order(request, pk):
    client = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=client).order_by('-created')
    prod_dict = {}
    for order in orders:
        products = order.products.filter(order=order.pk)
        product_set = set()
        for product in products:
            product_set.add(product.name)
        prod_dict[order.pk] = product_set
    return render(request, 'order.html', {
        'client': client,
        'orders': orders,
        'products': prod_dict}
                  )


def client_order_products(request, pk: int, days: int):
    product_set = set()
    now = timezone.now()
    before = now - timedelta(days=days)
    client = get_object_or_404(Client, pk=pk)
    orders = Order.objects.filter(client=client, created__gte=before)
    for order in orders:
        products = order.products.all()
        for product in products:
            product_set.add(product.name)
    print(product_set)

    return render(request, 'all_orders_prods.html',
                  {
                      'client': client,
                      'products': product_set,
                      'days': days})


def upload_image(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            fs = FileSystemStorage()
            fs.save(image.name, image)
    else:
        form = ImageForm()
    return render(request, 'second_hw_app/image_form.html', {'form': form})
