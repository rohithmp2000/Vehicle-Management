from django.shortcuts import redirect, render

from .models import Vehicle

from .forms import VehicleForm

# Create your views here.

def create(request):
    if request.method=="POST":
        form = VehicleForm(request.POST)  
        if form.is_valid():
            try:
                form.save() 
                return redirect('/list') 
            except Exception as e:
                print(e)
    else:
        form = VehicleForm()
        return render(request,'create.html',{'form':form})

def list(request):
    list=Vehicle.objects.all()
    return render(request,'list.html',{'list':list})

def update(request, id):  
    if request.method=="POST" :
        vehicletoedit = Vehicle.objects.get(id=id)  
        form = VehicleForm(request.POST, instance = vehicletoedit) 
        if form.is_valid():
            try:
                form.save() 
                return redirect('/list') 
            except Exception as e:
                print(e)
        return render(request,'edit.html', {'edit':vehicletoedit})
    vehicletoedit=Vehicle.objects.get(id=id)  
    return render(request,'edit.html', {'edit':vehicletoedit})