from django.shortcuts import render
from online.forms import registerform
from online.models import registermodel
# Create your views here.
def registerview(request):
    form = registerform
    if request.method=='POST':
        form = registerform(request.POST)
        if form.is_valid():
            #form.save()
            pass
    return render(request,'online.html',{'form':form})