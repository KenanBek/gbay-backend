# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers
from . import models


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ('title', 'price')


class CartSerializer(serializers.ModelSerializer):
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='cartitem-detail'
    )

    class Meta:
        model = models.Cart
        fields = ('id', 'author', 'status', 'items')


class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CartItem
        fields = ('cart', 'product', 'count')
