# from datetime import datetime
#
# from django.core.management.base import BaseCommand
# from django.shortcuts import get_object_or_404
# from second_hw_app.models import Order, Client
#
# import random
#
#
# class Command(BaseCommand):
#     help = "Generate fake client and orders."
#
#     def add_arguments(self, parser):
#         parser.add_argument('count', type=int, help='UserID')
#
#
#     def handle(self, *args, **kwargs):
#         count = kwargs.get('count')
#         for i in range(1, count + 1):
#             client = Client(name=f'Name{i}', email=f'mail{i}@mail.ru',
#                             phone_number=f'129837{i}', address=f'city{i}', registered=datetime.now())
#             client.save()
#         for j in range(1, count + 1):
#             order = Order(client=client, product=f'products {j}', total_amount=f'100+{j}', created=datetime.now())
#             order.save()
