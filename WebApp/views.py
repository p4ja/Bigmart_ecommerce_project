from django.shortcuts import render,redirect
from Backend.models import (Product_db,category_db)
from WebApp.models import Contact_db,registration_db,cart_db,place_orderdb
from django.contrib import messages
import razorpay
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
        messages.success(req, "contact saved succesfully..")
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
            messages.success(request, "login successfully..")
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
    subtotal=0
    shipping_charge=0
    total=0
    for d in data:
        subtotal=subtotal+d.total_price
        if subtotal>=500:
            shipping_charge=50
        else:
            shipping_charge=100
        total=shipping_charge + subtotal
    return render(request,"cart.html",{'data':data,'subtotal':subtotal,'shipping_charge':shipping_charge,'total':total})

def delete_cart(req,p_id):
    x=cart_db.objects.filter(id=p_id)
    x.delete()
    messages.error(req,"deleted successfully...")
    return redirect(cart_page)

def userlogin_page(req):
    return render(req,"user_login.html")
def checkout_page(request):
    data=cart_db.objects.filter(username=request.session['username'])
    subtotal = 0
    shipping_charge = 0
    total = 0
    for d in data:
        subtotal = subtotal + d.total_price
        if subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total = shipping_charge + subtotal
    return render(request,"checkout.html",{'data':data,'subtotal':subtotal,'shipping_charge':shipping_charge,'total':total})

def payment_page(request):
    #retrieve the place_orderdb object with the specified Id
    customer=place_orderdb.objects.order_by('-id').first()

    #get the payment amount of the specified customer
    pay=customer.total_price

    #convert the amount to paisa (smallest currency unit)
    amount=int(pay*100)                  #Assuming payment amount in rupees

    #convert amount to string for printing
    pay_str=str(amount)


    #printing each character of the payment amount
    for i in pay_str:
        print(i)
    if request.method=="POST":
        order_currency='INR'
        client=razorpay.Client(auth=('rzp_test_VuEafQLHBKrSGH','vbTtWMTJU57Kcl8U7GP2bLa2'))
        payment=client.order.create({'amount':amount,'currency':order_currency,'payment_capture':'1'})
    return render(request,"payment.html",{'customer':customer,'pay_str':pay_str})

def save_placeorder(request):
    if request.method=="POST":
        na=request.POST.get('Name')
        em=request.POST.get('email')
        add=request.POST.get('Address')
        pho=request.POST.get('Phone')
        bill=request.POST.get('bill')
        tp=request.POST.get('total')
        obj=place_orderdb(Name=na,email=em,Address=add,Phone=pho,bill=bill,total_price=tp)
        obj.save()
        return redirect(payment_page)