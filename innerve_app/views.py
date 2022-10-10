from email import contentmanager
from turtle import bgcolor
from django.shortcuts import render,redirect,HttpResponse
from .models import Doctor, Patient
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
def authenticate(email,password):
    patient=Patient.objects.filter(email=email,password=password)
    return patient
def authenticatedoc(email,password):
    doc=Doctor.objects.filter(email=email,password=password)
    return doc

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
        return redirect('login')
        
    return render(request,"patient.html")
def doctor(request):
    if request.method=="POST":
        
        dname = request.POST['dname']
        email = request.POST['email']
        password=request.POST['password']
        dob = request.POST['dob']
        phone=request.POST['phone']
        profile = request.POST['profile']
        category = request.POST['category']
        qualification = request.POST['qualification']
        fee= request.POST['fee']
        doctor = Doctor(dname=dname, email=email, password=password,dob=dob, phone=phone,profile=profile,qualification=qualification,fee=fee,category=category)
        doctor.save()
        messages.success(request, " You have been registered!")
        return redirect('login')
    return render(request,'doctor.html')

def free(request):
    return render(request,'free.html')
def paid(request):
    return render(request,'paid.html')
def login(request):
    if request.method=="POST":
        loginusername=request.POST['email']
        loginpassword=request.POST['password']
        user=authenticate(email=loginusername,password=loginpassword)
        print(user)
        if len(user)>0:
            return render(request,"mainpage.html")
        else:
            messages.error(request,"Invalid credentials!")

    return render(request,'login.html')

def logindoc(request):
    if request.method=="POST":
        loginusername=request.POST['email']
        loginpassword=request.POST['password']
        use=authenticatedoc(email=loginusername,password=loginpassword)
        print(use)
        if len(use)>0:
            return render(request,"mainpagedoc.html")
        else:
            messages.error(request,"Invalid credentials!")

    return render(request,'logindoc.html')

def bot(request):
    return render(request,'bot.html')
def mainpage(request):
    alldoc=Doctor.objects.all()
    context={'doc':alldoc}
    return render(request,'mainpage.html',context)
def mainpagedoc(request):
    return render(request,"mainpagedoc.html")

def ambulance(request):
    
    return render(request,"ambulance.html")
    
