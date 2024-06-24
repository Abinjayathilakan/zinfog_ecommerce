from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('list_products',views.list_products,name='list_products'),
    path('product_details/<pk>',views.detail_product,name='detail_product'),
    
    path('product', views.product, name='product'),
    path('add_details/', views.add_details, name='add_details'),
    path('show_products', views.show_products, name='show_products'),
    path('edit_product/<int:ab>/', views.edit_product, name='edit_product'),
    path('edit_product_details/<int:ab>/', views.edit_product_details, name='edit_product_details'),
    path('delete_product/<int:ab>/',views.delete_product,name='delete_product'),
]
