from django.db import models

# Create your models here.


class registermodel(models.Model):
    username =models.CharField(max_length=30, unique=True)
    firstname= models.CharField(max_length=30)
    email =models.EmailField(max_length=30,unique=True)
    gender =models.CharField(max_length=30)
    dob= models.DateField()
    age= models.IntegerField()
    phone=models.BigIntegerField(unique=True)
    address=models.CharField(max_length=30)
    password =models.CharField(max_length=30)
