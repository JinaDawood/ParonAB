from django.contrib import admin
from .models import Product, Inventory, Balance, Delivery

admin.site.register(Product)
admin.site.register(Inventory)
admin.site.register(Balance)
admin.site.register(Delivery)
