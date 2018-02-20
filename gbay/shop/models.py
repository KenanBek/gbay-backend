# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=128)
    price = models.DecimalField(
        max_digits=10, decimal_places=2,
        default=0.00,
        db_index=True
    )
    amount = models.PositiveSmallIntegerField(default=1)

    def __unicode__(self):
        return u"{} ({})".format(self.title, self.amount)


class Cart(models.Model):
    STATUS_OPEN = 1
    STATUS_APPROVED = 2
    STATUS_CANCELED = 3
    STATUS_CLOSED = 4
    STATUS_CHOICES = (
        (STATUS_OPEN, 'Open'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_CANCELED, 'Cancelled'),
        (STATUS_CLOSED, 'Closed'),
    )

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES)

    def __unicode__(self):
        return u"cart#{}".format(self.id)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product)
    count = models.IntegerField(default=0)

    def __str__(self):
        return "{} x {} ({})".format(self.product, self.count, self.cart)
