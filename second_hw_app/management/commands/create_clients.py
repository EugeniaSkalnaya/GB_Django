from django.core.management.base import BaseCommand
from second_hw_app.models import Client


class Command(BaseCommand):
    help = "Create clients."

    def handle(self, *args, **kwargs):
        for i in range(10):
            client = Client(
                name=f'client {i}',
                email=f'{i}@example.com',
                phone_number=f"123{i}567",
                address=f'City{i} Street House Flat')
            client.save()
            self.stdout.write(f'{client}')
