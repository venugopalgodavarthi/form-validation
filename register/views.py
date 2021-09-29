from django.shortcuts import render
from register.forms import registerform
from register.models import registermodel
# Create your views here.
def registerview(request):
    if request.method =='GET':
        form = registerform(None)
    if request.method =='POST':
        form = registerform(request.POST)
        print("username",request.POST['username'])
        print("firstname",request.POST['firstname'])
        print("email",request.POST['email'])
        print("phone",request.POST['phone'])
        print("age",request.POST['age'])
        print("address",request.POST['address'])
        print("dob",request.POST['dob'])
        print("gender",request.POST['gender'])
        username = request.POST['username']
        firstname = request.POST['firstname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        address = request.POST['address']
        dob = request.POST['dob']
        gender = request.POST['gender']
        password = request.POST['password']
        res = registermodel.objects.create(username = username, firstname=firstname,
                                           email=email,phone=phone,age=age,address=address,dob=dob,
                                           gender=gender,password=password)
        res.save()
    return render(request,'register.html',{'form':form})