from django.contrib import admin
from myapp.models import student,stu,trainer,trainer2,child2,son
# Register your models here.

class studentadmin(admin.ModelAdmin):
    list_display= ['id','sname','email','phone']


admin.site.register(student,studentadmin)

class stuadmin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','address','subject','marks']


admin.site.register(stu,stuadmin)

class traineradmin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','address','tsubject','sal']


admin.site.register(trainer,traineradmin)

class trainer2admin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','address','adhar','pincode']


admin.site.register(trainer2,trainer2admin)

class child2admin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','address','adhar','pincode','pan','passport']


admin.site.register(child2,child2admin)


class sonadmin(admin.ModelAdmin):
    list_display= ['id','name','email','phone','address','m_id','adhar','pincode','pan','passport']
admin.site.register(son,sonadmin)