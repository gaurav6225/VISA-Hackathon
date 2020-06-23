from django.db import models
from django.contrib.auth.models import User

class UserRegistration(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_merchant = models.BooleanField(default = False, blank = True)
    address = models.CharField(max_length=500)
    zipcode = models.CharField(max_length=6)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    
    def __str__(self):
        return self.user.username

class Product(models.Model):
    merchant = models.ForeignKey('UserRegistration', on_delete=models.CASCADE, null = True)
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300, null = True)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,default="")
    phone=models.CharField(max_length=50,default="")
    desc=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    items_json=models.CharField(max_length=5000)
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    zipcode=models.CharField(max_length=100)
    phone=models.CharField(max_length=50,default="")
   
