
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('add_product/',views.add_product,name='add_product'),
    path('create_order/',views.create_order,name='create_order'),
]
