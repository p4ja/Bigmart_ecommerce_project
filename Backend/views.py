from django.shortcuts import render,redirect
from Backend.models import category_db,Product_db
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from WebApp.models import Contact_db
from django.contrib import messages
# Create your views here.
def index_page(req):
    return render(req,"index.html")
def add_category(req):
    return render(req,"add_category.html")

def save_category(req):
    if req.method=="POST":
        cn=req.POST.get('CategoryName')
        desc=req.POST.get('Description')
        img=req.FILES['Fileupload']
        obj=category_db(CategoryName=cn,Description=desc,Fileupload=img)
        obj.save()
        messages.success(req,"category saved successfully..")
        return redirect(add_category)

def display_category(req):
    data=category_db.objects.all()
    return render(req,"display_category.html",{'data':data})

def edit_category(req,cat_id):
    data=category_db.objects.get(id=cat_id)
    return render(req,"edit_category.html",{'data':data})

def update_category(req,cat_id):
    if req.method=="POST":
        cn=req.POST.get('CategoryName')
        des=req.POST.get('Description')
        try:
            img=req.FILES['Fileupload']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=category_db.objects.get(id=cat_id).Fileupload
        category_db.objects.filter(id=cat_id).update(CategoryName=cn,Description=des,Fileupload=file)
        messages.warning(req,'category updated successfully..')
        return redirect(display_category)

def delete_category(req,cat_id):
    x=category_db.objects.filter(id=cat_id)
    x.delete()
    messages.error(req,"deleted successfully..")
    return redirect(display_category)

def login_page(req):
    return render(req,"admin_login.html")

def admin_login(request):
    if request.method=="POST":
        un=request.POST.get('username')
        pwd=request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x=authenticate(username=un,password=pwd)
            if x is not None:
                login(request,x)
                request.session['username']=un
                request.session['password']=pwd
                messages.success(request,"welcome..")
                return redirect(index_page)
            else:
                messages.error(request,"invalid password..")
                return (login_page)
        else:
            messages.warning(request,"user not found..")
            return redirect(login_page)

def admin_logout(request):
    del request.session['username']
    del request.session['password']
    messages.success(request,"logout successfully..")
    return redirect(login_page)

def product_page(req):
    cat=category_db.objects.all
    return render(req,"products.html",{'cat':cat})

def save_product(req):
    if req.method=="POST":
        pn=req.POST.get('ProductName')
        pc=req.POST.get('ProductCategory')
        pri=req.POST.get('Price')
        des=req.POST.get('Description')
        img=req.FILES['ProductImage']
        obj=Product_db(ProductName=pn,ProductCategory=pc,Price=pri,Description=des,ProductImage=img)
        obj.save()
        messages.success(req,'product saved successfully..')
        return redirect(product_page)

def display_product(req):
    data=Product_db.objects.all()
    return render(req,"display_product.html",{'data':data})

def edit_product(req,prod_id):
    data=Product_db.objects.get(id=prod_id)
    cat=category_db.objects.all()
    return render(req,"edit_product.html",{'data':data,'cat':cat})

def update_product(req,prod_id):
    if req.method=="POST":
        proname=req.POST.get('ProductName')
        procat=req.POST.get('ProductCategory')
        pric=req.POST.get('Price')
        desc=req.POST.get('Description')
        try:
            img=req.FILES['ProductImage']
            fs=FileSystemStorage()
            file=fs.save(img.name,img)
        except MultiValueDictKeyError:
            file=Product_db.objects.get(id=prod_id).ProductImage
        Product_db.objects.filter(id=prod_id).update(ProductName=proname,ProductCategory=procat,Price=pric,Description=desc,ProductImage=file)
        messages.warning(req,'product updated successfully..')
        return redirect(display_product)

def delete_product(req,prod_id):
    x=Product_db.objects.filter(id=prod_id)
    x.delete()
    messages.error(req,'product deleted successfully..')
    return redirect(display_product)

def contact_details(req):
    data=Contact_db.objects.all()
    return render(req,"contact_data.html",{'data':data})

def delete_contact(req,cont_id):
    x=Contact_db.objects.filter(id=cont_id)
    x.delete()
    return redirect(contact_details)






