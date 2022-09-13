from django.contrib import admin

from .models import Construction, Project

class ConstructionAdmin(admin.ModelAdmin):
    list_display = ['project' ,'reference_name','id', 'category', 'width' , 'height', 'color', 'slug']
    prepopulated_fields = {'slug': ('reference_name', 'width', 'height')}

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name','id', 'price' ,'slug']

admin.site.register(Construction, ConstructionAdmin)
admin.site.register(Project, ProjectAdmin)
