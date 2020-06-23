from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('contact/', views.contact, name="ShopHome"),
    path('products/<int:id>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
]