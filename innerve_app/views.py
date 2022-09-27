from email import contentmanager
from turtle import bgcolor
from django.shortcuts import render,redirect,HttpResponse
from .models import Doctor, Patient
from django.contrib import messages

def index(request):
    return render(request,'first.html')
def choose(request):
    return render(request,'first.html')
def patient(request):
    #thank = False
    if request.method=="POST":
        
        pname = request.POST['pname']
        email = request.POST['email']
        dob = request.POST['dob']
        pf=request.POST['pf']
        bg = request.POST['bg']
        content = request.POST['content']
        extra = request.POST['extra']
        password = request.POST['password']
        patient = Patient(pname=pname, email=email, dob=dob,pf=pf, bg=bg,content=content,extra=extra, password=password)
        patient.save()
        messages.success(request, " The patient has been registered!")
        
    return render(request,"patient.html")
def doctor(request):
    if request.method=="POST":
        
        dname = request.POST['dname']
        email = request.POST['email']
        dob = request.POST['dob']
        phone=request.POST['phone']
        profile = request.POST['profile']
        category = request.POST['category']
        qualification = request.POST['qualification']
        fee= request.POST['fee']
        doctor = Doctor(dname=dname, email=email, dob=dob, phone=phone,profile=profile,qualification=qualification,fee=fee,category=category)
        doctor.save()
        messages.success(request, " You have been registered!")
    return render(request,'doctor.html')

def free(request):
    return render(request,'free.html')
def paid(request):
    return render(request,'paid.html')
def login(request):
    return render(request,'login.html')
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username=loginusername,password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,"Successfully Logged In")
            return redirect("home")
        else:
            messages.error(request,"Invalid credentials!")
            return redirect("home")

    return HttpResponse("404- Not Found")

def bot(request):
    return render(request,'bot.html')


