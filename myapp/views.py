from django.shortcuts import render
from myapp.forms import log
# Create your views here.

def login(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request,'base.html')


def loginform(request):
    form=log
    return render(request,'log.html',{'form':form})
    