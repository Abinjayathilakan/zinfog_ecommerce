from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('show_cart',views.show_cart,name='show_cart'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    path('remove_item_cart/<pk>',views.remove_item_cart,name='remove_item_cart'),
    path('checkout_cart',views.checkout_cart,name='checkout_cart'),
    path('show_orders',views.show_orders,name='show_orders'),
]
