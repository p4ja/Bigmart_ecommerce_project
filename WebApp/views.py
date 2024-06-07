from django.shortcuts import render,redirect
from Backend.models import (Product_db,category_db)
from WebApp.models import Contact_db,registration_db,cart_db
from django.contrib import messages
# Create your views here.
def home_page(req):
    cat=category_db.objects.all()
    return render(req,"home.html",{'category':cat})

def about_page(req):
    cat = category_db.objects.all()
    return render(req,"about.html",{'cat':cat})

def contact_page(req):
    return render(req,"contact.html")

def save_contact(req):
    if req.method=="POST":
        na=req.POST.get('name')
        em=req.POST.get('email')
        pho=req.POST.get('phone')
        sub=req.POST.get('subject')
        mes=req.POST.get('message')
        obj=Contact_db(name=na,email=em,phone=pho,subject=sub,message=mes)
        obj.save()
        return redirect(contact_page)

def our_products(req):
    cat = category_db.objects.all()
    pro=Product_db.objects.all()
    return render(req,"our_products.html",{'products':pro,'cat':cat})



def filtered_product(req,cat_name):
    data=Product_db.objects.filter(ProductCategory=cat_name)
    return render(req,"product_filtered.html",{'data':data})
def single_product(req,prod_id):
    data=Product_db.objects.get(id=prod_id)
    return render(req,"single_product.html",{'data':data})

def registeration_page(req):
    return render(req,"register.html")


def save_registeration(req):
    if req.method=="POST":
        un=req.POST.get('username')
        em=req.POST.get('email')
        pwd=req.POST.get('password')
        cpwd=req.POST.get('confirm_password')
        img=req.FILES['profileimage']
        obj=registration_db(username=un,email=em,password=pwd,confirm_password=cpwd,profileimage=img)
        if registration_db.objects.filter(username=un).exists():
            messages.warning(req,"username already exists..")
            return redirect(registeration_page)
        elif registration_db.objects.filter(email=em).exists():
            messages.warning(req,"email id already exists..")
            return redirect(registeration_page)
        else:
            obj.save()
            messages.success(req,"registered succesfully..")
        return redirect(registeration_page)

def Userlogin(request):
    if request.method=="POST":
        un=request.POST.get('uname')
        pwsd=request.POST.get('password')
        if registration_db.objects.filter(username=un,password=pwsd).exists():
            request.session['username']=un
            request.session['password']=pwsd
            return redirect(home_page)
        else:
            return redirect(registeration_page)
    else:
        return redirect(registeration_page)

def userlogout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logoout succesfully..")
    return redirect(home_page)

def save_cart(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pn=request.POST.get('ProductName')
        qua=request.POST.get('quantity')
        tp=request.POST.get('total_price')
        obj=cart_db(username=un,ProductName=pn,quantity=qua,total_price=tp)
        obj.save()
        messages.success(request, "saved succesfully..")
        return redirect(home_page)

def cart_page(request):
    data=cart_db.objects.filter(username=request.session['username'])
    total=0
    for d in data:
        total=total+d.total_price
    return render(request,"cart.html",{'data':data,'total':total})

def delete_cart(req,p_id):
    x=cart_db.objects.filter(id=p_id)
    x.delete()
    messages.error(req,"deleted successfully...")
    return redirect(cart_page)

def userlogin_page(req):
    return render(req,"user_login.html")