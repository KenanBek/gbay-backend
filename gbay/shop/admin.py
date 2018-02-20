# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from . import models


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    pass


class CartItemInline(admin.TabularInline):
    model = models.CartItem

    readonly_fields = ['cart', ]

    extra = 1
    can_delete = False


@admin.register(models.Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = [CartItemInline, ]
