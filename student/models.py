from django.db import models

# Create your models here.

# img=models.ImageField(upload_to='media/product',default=True)

class student_register(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=200)
    dob=models.CharField(max_length=200)
    gender=models.CharField(max_length=200)
    relegion=models.CharField(max_length=200)
    adhar=models.ImageField(max_length=200)
    photo=models.ImageField(max_length=200)
    address=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    pincode=models.IntegerField(null=True)
    guardianname=models.CharField(max_length=200)
    guardianmobile=models.CharField(max_length=200)
    sslccertificate=models.ImageField(max_length=200)
    sslcpassoutyear =models.CharField(max_length=200)
    schoolname =models.CharField(max_length=200)
    schoollocation =models.CharField(max_length=200)
    hss_name =models.CharField(max_length=200)
    hsscertificate=models.ImageField(max_length=200)
    hsspersentage=models.CharField(max_length=200)
    hsspassoutyear=models.CharField(max_length=200)      