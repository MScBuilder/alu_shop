from django.contrib import admin

from .models import Construction, OrderItem, Order

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'color', 'width' , 'height']
    prepopulated_fields = {"slug": ("title", "width", "height")}

admin.site.register(Construction, ConstructionAdmin)
admin.site.register(OrderItem)
admin.site.register(Order)
