
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('products/', views.products, name='products'),
    path('customer/<str:pk>/',views.customer,name='customer'),
    path('add_product/',views.add_product,name='add_product'),
    path('create_order/<str:pk>/',views.create_order,name='create_order'),
    path('update_order/<str:pk>/',views.update_order,name='update_order'),
    path('delete_order/<str:pk>/',views.delete_order,name='delete_order')
]
