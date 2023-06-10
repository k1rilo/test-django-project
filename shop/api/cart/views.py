from django.shortcuts import render
from .models import Cart
from .serializers import CartSerializer
from rest_framework import generics



class CartList(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDelete(generics.DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartCreate(generics.CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


