from django import forms
from django.contrib.auth.models import User
from shop.models import UserRegistration
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class UserForm(UserCreationForm):
    first_name = forms.CharField(max_length=500)
    last_name = forms.CharField(max_length=500)
    address = forms.CharField(max_length=500)
    zipcode = forms.CharField(max_length=500)
    phone = forms.CharField(max_length=500)
    city = forms.CharField(max_length=500)
    state = forms.CharField(max_length=500)
    is_merchant = forms.BooleanField()
    class Meta():
        model=get_user_model()
        fields=('username','first_name','last_name','email','password1','password2','is_merchant','address',
        'zipcode','phone','city','state')