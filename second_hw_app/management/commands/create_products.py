from random import randint

from django.core.management.base import BaseCommand
from second_hw_app.models import Product


class Command(BaseCommand):
    help = "Create different products"

    def handle(self, *args, **kwargs):
        for i in range(50):
            product = Product(
                name=f'Name {i}',
                description=f'description of {i} product',
                price=randint(1, 10000),
                count=randint(1, 5)
            )
            product.save()
            self.stdout.write(f'{product}')