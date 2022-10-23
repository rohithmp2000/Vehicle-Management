from django.shortcuts import render

from .forms import VehicleForm

# Create your views here.

def Vehicle(request):
    form = VehicleForm()  
    return render(request,'html1.html',{'form':form})
