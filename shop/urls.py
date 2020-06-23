from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('contact/', views.contact, name = "ShopContact"),
    path('products/<int:id>', views.productView, name="ProductView"),
    path('checkout/', views.checkout, name="Checkout"),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name='register'),
]