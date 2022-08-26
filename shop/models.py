from statistics import mode
from tkinter import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.shortcuts import reverse
from django.conf import settings
from django.db import models
from .validators import MaxWidthValidator

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

FIX_MAX_WIDTH: int = 2500
FIX_MIX_WIDTH: int = 300
FIX_MAX_HEIGHT: int= 3500
FIX_MIN_HEIGHT: int = 300

CASEMENT_MAX_WIDTH: int = 2500
CASEMENT_MIX_WIDTH: int = 1000
CASEMENT_MAX_HEIGHT: int = 2300
CASEMENT_MIN_HEIGHT: int = 800

SLIDE_MAX_WIDTH: int = 4000
SLIDE_MIX_WIDTH: int = 1200
SLIDE_MAX_HEIGHT: int = 2500
SLIDE_MIN_HEIGHT: int = 1200


class Construction(models.Model):
    category = models.CharField(choices=CATEGORY_CHOICES, default="CW", max_length=2)
    title = models.CharField(max_length=100)
    width = models.PositiveIntegerField(default=1000, 
                                        validators=[MaxWidthValidator(FIX_MAX_WIDTH, "you are stupid", "CW")])
    height = models.PositiveIntegerField(default=1000, 
                                        validators=[
                                                MaxValueValidator(3000),
                                                MinValueValidator(350)
                                            ])
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