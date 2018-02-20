# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets

from . import models
from . import serializers


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = models.Product.objects.all().order_by('-id')
    serializer_class = serializers.ProductSerializer


class CartViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows carts to be viewed or edited.
    """
    queryset = models.Cart.objects.all().order_by('-id')
    serializer_class = serializers.CartSerializer
