from django.db import models

# Create your models here.
class Contact_db(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    phone=models.IntegerField(null=True,blank=True)
    subject=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(null=True,blank=True)

class registration_db(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    confirm_password=models.CharField(max_length=100,null=True,blank=True)
    profileimage=models.ImageField(upload_to='profileimage',null=True,blank=True)


class cart_db(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)

class place_orderdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    Address=models.CharField(max_length=100,null=True,blank=True)
    Phone=models.IntegerField(null=True,blank=True)
    bill=models.TextField(null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)
