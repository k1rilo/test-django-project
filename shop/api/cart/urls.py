from django.contrib import admin
from django.urls import path
from .views import CartList, CartDelete, CartUpdate, CartCreate

urlpatterns = [
    path('cart/', CartList.as_view(), name='cart-list'),
    path('cart/create/',
         CartCreate.as_view(), name='cart-create'),
    path('cart/delete/<int:pk>/',
         CartDelete.as_view(), name='cart-delete'),
    path('cart/update/<int:pk>/',
         CartUpdate.as_view(), name='cart-update'),
]