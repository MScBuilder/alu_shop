from django.shortcuts import reverse
from django.conf import settings
from django.db import models
<<<<<<< HEAD

import aluminium_system_info.size_restrictions

CATEGORY_CHOICES = {
    ('FW', 'Fix window'),
    ('CW', 'Casement window'),
    ('SW', 'Sliding window'),
}

COLOR_CHOICES = {
    ('9016', 'White'),
    ('9006', 'Silver'),
    ('9005', 'Black'),
    ('8017', 'Brown'),
    ('7016', 'Antracite')
}
=======
from .validators import width_validator, height_validator
from shop.aluminium_system_info.color_options import COLOR_CHOICES
from shop.aluminium_system_info.category_options import CATEGORY_CHOICES
>>>>>>> work_new_view


class Construction(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, default="FW", max_length=2)
    reference_name = models.CharField(max_length=100, unique=True)
    width = models.PositiveIntegerField(default=1000, 
                                        validators=[width_validator])
    height = models.PositiveIntegerField(default=1000, 
                                        validators=[height_validator])
    price = models.FloatField()
    color = models.CharField(choices=COLOR_CHOICES, default="9016", max_length=4)
    slug = models.SlugField(max_length=200)
    
    def __str__(self):
        return self.reference_name
    
    def get_absolute_url(self):
        return reverse('core:product_page', kwargs={'slug': self.slug})
 
class Qutation(models.Model):
    construction = models.ForeignKey(Construction, on_delete=models.CASCADE)
    #slug = models.SlugField()
    
    def __str__(self):
        return self.item.title
    
    def get_absolute_url(self):
        return reverse('core:quotation_page')
     
    
class OrderItem(models.Model):
    item = models.ForeignKey(Construction, on_delete=models.CASCADE)

    def __str__(self):
        return self.item.reference_name

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username