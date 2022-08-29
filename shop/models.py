from django.shortcuts import reverse
from django.conf import settings
from django.db import models
from .validators import width_validator, height_validator
from shop.aluminium_system_info.color_options import COLOR_CHOICES
from shop.aluminium_system_info.category_options import CATEGORY_CHOICES


class Construction(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, default="CW", max_length=2)
    title = models.CharField(max_length=100)
    width = models.PositiveIntegerField(default=1000, 
                                        validators=[width_validator])
    height = models.PositiveIntegerField(default=1000, 
                                        validators=[height_validator])
    price = models.FloatField()
    color = models.CharField(choices=COLOR_CHOICES, default="9016", max_length=4)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('core:product_page', kwargs={'slug': self.slug})
    
    
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