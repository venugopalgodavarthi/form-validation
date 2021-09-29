from django.contrib import admin
from register.models import registermodel

# Register your models here.
class registermodeladmin(admin.ModelAdmin):
    list_display=['id','username','firstname','email','phone','age','gender','dob','address','password']
    
admin.site.register(registermodel,registermodeladmin)