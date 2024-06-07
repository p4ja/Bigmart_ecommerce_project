from django.db import models

# Create your models here.
class category_db(models.Model):
    CategoryName=models.CharField(max_length=100,null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    Fileupload=models.ImageField(upload_to="file_upload",null=True,blank=True)

class Product_db(models.Model):
    ProductName=models.CharField(max_length=100,null=True,blank=True)
    ProductCategory=models.CharField(max_length=100,null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    ProductImage=models.ImageField(upload_to='ProductImage',null=True,blank=True)
