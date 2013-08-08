#encoding: utf-8

from django.views.generic import DetailView, ListView

from .models import Product


class Catalog1(DetailView):

    template_name = 'catalog/product.html'
    queryset = Product.objects.filter(price__isnull=False)
    context_object_name = 'product'
    
    # def get_queryset(self):
    #     return Product.objects.filter(price__isnull=False)


class Catalog2(ListView):

    template_name = 'catalog/list.html'

    paginate_by = 2

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        #queryset = Product.objects.filter(user=self.request.user)
        return Product.objects.filter(price__isnull=False)