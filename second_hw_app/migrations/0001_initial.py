# Generated by Django 5.0.3 on 2024-04-05 09:30

import django.core.validators
import django.db.models.deletion
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("email", models.EmailField(max_length=150, verbose_name="Email")),
                (
                    "phone_number",
                    models.IntegerField(
                        blank=True, null=True, verbose_name="Phone number"
                    ),
                ),
                (
                    "address",
                    models.TextField(blank=True, null=True, verbose_name="Address"),
                ),
                (
                    "registered",
                    models.DateTimeField(auto_now_add=True, verbose_name="Registered"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Name")),
                ("description", models.TextField(verbose_name="Description")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=8,
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=Decimal(
                                    "0.1000000000000000055511151231257827021181583404541015625"
                                )
                            )
                        ],
                        verbose_name="Price",
                    ),
                ),
                (
                    "count",
                    models.PositiveIntegerField(
                        default=1, verbose_name="Number of products"
                    ),
                ),
                (
                    "added",
                    models.DateTimeField(auto_now_add=True, verbose_name="Added date"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "total_amount",
                    models.DecimalField(
                        decimal_places=2,
                        default=0,
                        max_digits=10,
                        verbose_name="Total amount",
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="second_hw_app.client",
                        verbose_name="client",
                    ),
                ),
                (
                    "product",
                    models.ManyToManyField(
                        to="second_hw_app.product", verbose_name="Products"
                    ),
                ),
            ],
        ),
    ]
