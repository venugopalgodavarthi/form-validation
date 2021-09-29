from django.db import models
'''
# Create your models here.
class student(models.Model):
    sname=models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    phone =models.BigIntegerField()
    
    
class details(models.Model):
    name=models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    phone =models.BigIntegerField()
    address=models.CharField(max_length=30)
    class Meta:
        abstract =True
        
class stu(details):
    subject = models.CharField(max_length=30)
    marks =models.IntegerField()
    
class trainer(details):
    tsubject = models.CharField(max_length=30)
    sal =models.FloatField()
    
    
class content(models.Model):
    name=models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    phone =models.BigIntegerField()
    address=models.CharField(max_length=30)
    
class trainer2(content):
    adhar = models.BigIntegerField()
    pincode =models.IntegerField()
    
class super1(models.Model):
    name=models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    phone =models.BigIntegerField()
    address=models.CharField(max_length=30)

class child1(super1):
    adhar = models.BigIntegerField()
    pincode =models.IntegerField()
    
class child2(child1):
    pan = models.BigIntegerField()
    passport =models.IntegerField()
    

class father(models.Model):
    name=models.CharField(max_length=30)
    email =models.EmailField(max_length=30)
    phone =models.BigIntegerField()
    address=models.CharField(max_length=30)

class mother(models.Model):
    m_id =models.IntegerField(primary_key=True)
    adhar = models.BigIntegerField()
    pincode =models.IntegerField()
    
class son(father,mother):
    pan = models.BigIntegerField()
    passport =models.IntegerField()

  '''  
    