from django.urls import path
from .views import *


urlpatterns = [
    path('categories/', CategoriesApiView.as_view(), name='categoriesapiview'),
    path('category/<str:slug>/', CategoryApiView.as_view(), name='categoryapiview'),
    path('products/', ProductsApiView.as_view(), name='productsapiview'),
    path('product/<str:slug>/', ProductApiView.as_view(), name='productapiview'),
    path('customers/', CustomersApiView.as_view(), name='customersapiview'),
    path('customer/<str:email>/', CustomerApiView.as_view(), name='customerapiview'),
    path('inventories/', InvertoriesApiView.as_view(), name='inventoriesapiview'),
    path('inventory/<int:pk>/', InventoryApiView.as_view(), name='inventoryapiview'),
    path('orders/', OrdersApiView.as_view(), name='ordersapiview'),
    path('order/<int:pk>/', OrderApiView.as_view(), name='orderapiview'),
    path('pps/', PPSApiView.as_view(), name='ppsapiview'),
    path('pp/<int:pk>/', PPApiView.as_view(), name='ppapiview')
]