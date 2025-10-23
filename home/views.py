from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Departments,Doctors
from .forms import BookingForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):

    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

@login_required
def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    else:
        form=BookingForm()

    return render(request,'booking.html',{'form':form})

def doctors(request):
    dict_docs ={
        'doctors':Doctors.objects.all()
    }
    return render(request,'doctors.html',dict_docs)

def contact(request):
    return render(request,'contact.html')

def  department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request,'department.html',dict_dept)