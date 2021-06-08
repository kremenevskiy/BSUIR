from django.contrib import admin
from django import forms

# Register your models here.

from .models import *

admin.site.register(Category)
admin.site.register(Notebook)
admin.site.register(Smartphone)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)





class NotebookCategoryChoiceFieldmod(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return NotebookCategoryChoiceFieldmod(Category.objects.filter(slug='notebook'))
        return super().formfield_for_foreignkey(db_field, **kwags)