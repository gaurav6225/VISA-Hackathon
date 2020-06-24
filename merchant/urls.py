from django.urls import path
from . import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordChangeView

app_name='merchant'

urlpatterns = [
    path('', views.index, name='home'),
    path('merchant', views.index, name='home'),
    path('merchant/<int:order_id>/', views.show, name='show'),
    path('merchant/new/', views.new, name='new'),
    path('merchant/edit/<int:order_id>/', views.edit, name='edit'),
    path('merchant/delete/<int:order_id>/', views.destroy, name='delete'),
    path('users/logout/', LogoutView.as_view, {'next_page': '/'}, name='logout'),
    path('users/change_password/', PasswordChangeView.as_view,
         {'post_change_redirect': '/', 'template_name': 'change_password.html'}, name='change_password'),
]