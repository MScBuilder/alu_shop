from django.contrib import admin

from .models import Construction, OrderItem, Order

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ['reference_name','id', 'category', 'width' , 'height', 'color', 'slug']
    prepopulated_fields = {'slug': ('reference_name', 'width', 'height')}

admin.site.register(Construction, ConstructionAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
