from django.contrib import admin

from .models import Construction, OrderItem, Order

admin.site.register(Construction)
admin.site.register(OrderItem)
admin.site.register(Order)
