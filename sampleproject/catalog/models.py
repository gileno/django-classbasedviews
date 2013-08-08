#encoding: utf-8

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=8, null=True,
        blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']