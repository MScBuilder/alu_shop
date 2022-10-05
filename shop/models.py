from django.shortcuts import reverse
from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
from .validators import width_validator, height_validator
from .aluminium_system_info.price_calculations import construction_calculate_price, project_calculate_price
from shop.aluminium_system_info.color_options import COLOR_CHOICES
from shop.aluminium_system_info.category_options import CATEGORY_CHOICES

class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True ,null=False)
    price = models.FloatField(default=0, null=False)
    slug = models.SlugField(null=True)
    
    def __str__(self):
        return self.name
    
    def get_update_url(self):
        return reverse('core:update_project', args=[str(self.id)])
        
    def get_name_url(self):
        return reverse('core:constructions_page', kwargs={'slug': self.name})
    
    def get_absolute_url(self):
        return reverse ('core:project_detail', kwargs={'pk': self.pk, 'category': 'all'})
    
    def get_delete_url(self):
        return reverse ('core:project_delete', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        if not self.slug:
            fields_to_slug = self.name
            self.slug = slugify(fields_to_slug)

        if self.id:
            self.price = project_calculate_price(self) 

        return super().save(*args, **kwargs)


class Construction(models.Model):
    project = models.ForeignKey('Project', on_delete=models.CASCADE, null=False, related_name='construction_project')
    category = models.CharField(choices=CATEGORY_CHOICES, default="FW", max_length=2)
    reference_name = models.CharField(max_length=100, unique=True)
    width = models.PositiveIntegerField(default=1000)
    height = models.PositiveIntegerField(default=1000)
    price = models.FloatField(null=True)
    color = models.CharField(choices=COLOR_CHOICES, default="9016", max_length=4)
    slug = models.SlugField(null=True)
    
    def clean(self):
        if self.category and self.width:
            width_validator(self.category, self.width)

        if self.category and self.height:
            height_validator(self.category, self.height)
            
        super().clean(self)
        return
    
    def __str__(self):
        return self.reference_name
        
    def get_absolute_url(self):
        return reverse('core:update_construction', kwargs={'pk': int(self.project.id), 'slug': self.slug})

    def get_proj_url(self):
        return reverse('core:project_detail', kwargs={'pk': self.project.id, 'category': 'all'})

    def save(self, *args, **kwargs):       
        if not self.slug:
            fields_to_slug = self.reference_name + "-" + str(self.width) + "-" + str(self.height)
            self.slug = slugify(fields_to_slug)       
        if not self.price:
            self.price = construction_calculate_price(self)       

        super().save(*args, **kwargs)
        self.project.save()
        return 
    
