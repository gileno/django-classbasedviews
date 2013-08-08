#encoding: utf-8

from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):

    list_display = ['name', 'slug', 'price']


admin.site.register(Product, ProductAdmin)