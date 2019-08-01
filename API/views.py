# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from items.models import Item, FavoriteItem
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ItemSerializer, ItemDetailSerializer
from .permissions import IsOwner


class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name',]
	permission_classes = [IsAuthenticated]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated,IsOwner]
	