from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as login_user
from .models import Product, Contact, Order, UserRegistration
from math import ceil
from django.urls import reverse, reverse_lazy
from .forms import UserForm


def register(request):

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Saving directly to DB
            user = user_form.save()
            # Hashing pass
            user.set_password(user.password)
            user.save()
            registered = True
            return HttpResponseRedirect(reverse('/shop/login/'))
        else:
            print(user_form.errors)

    # if request.method == 'GET':
    else:
        user_form = UserForm()

    return render(request, 'shop/register.html', {'user_form':user_form})



def home(request):
    return render(request,'shop/register.html')
	# return HttpResponseRedirect(reverse('register'))

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login_user(request,user)
            if user.is_merchant:
                return HttpResponseRedirect(reverse('merchant_homepage'))
            else:
                return HttpResponseRedirect(reverse('merchant_list'))
        else:
            messages.add_message(request,messages.ERROR,"Invalid password. Please try again.")
            return HttpResponseRedirect(reverse_lazy('login'))
    else:
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request,'shop/login.html')

@login_required
def merchant_list(request):
    user = UserRegistration.objects.filter(username=request.user.username)
    merchant_list = UserRegistration.objects.filter(is_merchant=True, zipcode=user[0].zipcode)
    return render(request, 'shop/merchant_list.html', {'merchant_list':merchant_list})

@login_required
def product_list(request,merchant_id):
    allProds=[]
    catprods= Product.objects.values('category','product_id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=Product.objects.filter(category=cat,merchant=merchant_id)
        n=len(prod)
        nSlides=n//4+ceil(n/4-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params = {'allProds':allProds}
    return render(request,'shop/index.html',params)

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        desc=request.POST.get('desc')
        contact= Contact(name=name, email=email,phone=phone, desc=desc)
        contact.save()
    return render(request, 'shop/contact.html')
def productView(request, id):
    product=Product.objects.filter(product_id=id)
    return render(request, 'shop/productView.html', {'product':product[0]})

@login_required
def checkout(request):
    if request.method=="POST":
        user = UserRegistration.objects.filter(username=request.user.username)
        items_json=request.POST.get('itemsJson')
        thank=True
        order=Order(items_json=items_json, name=user[0].name, email=user[0].email, phone=user[0].phone, address=user[0].address, state=user[0].state, zipcode=user[0].zipcode, city=user[0].city)
        order.save()
        return render(request, 'shop/checkout.html',{'thank':thank})
    return render(request, 'shop/checkout.html')
    
# Create your views here.
