from django.contrib import admin
from second_hw_app.models import Product, Client, Order


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    ordering = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    search_help_text = 'Поиск по имени клиента'
    readonly_fields = ['registered']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'count', 'added')
    ordering = ('name', '-added',)
    list_filter = ('name', 'price', 'added',)
    search_fields = ('name',)
    search_help_text = 'Поиск по названию продукта'
    readonly_fields = ('added',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('client', 'total_amount', 'created',)
    ordering = ('-created',)
    list_filter = ('client', 'created',)
    search_fields = ('created',)
    search_help_text = 'Поиск по дате заказа'
    readonly_fields = ['created']
