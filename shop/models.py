from statistics import mode
from tkinter import CASCADE
from django.conf import settings
from django.db import models

class Construction(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    
    def __str__(self):
        return self.title
    
class OrderItem(models.Model):
    item = models.ForeignKey(Construction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.title

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username