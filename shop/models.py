from statistics import mode
from tkinter import CASCADE
from django.conf import settings
from django.db import models

CATEGORY_CHOICES = {
    ('FW', 'fix window'),
    ('SW', 'Single window'),
    ('DW', 'Double window'),
    ('LS', 'Lift-slide window') 
}

LABEL_CHOICES = {
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
}


class Construction(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    category = models.CharField(max_length=2)
    category = models.CharField(choices=CATEGORY_CHOICES, default="FW", max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, default="P", max_length=1)
    
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