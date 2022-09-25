from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'first.html')
def choose(request):
    return render(request,'first.html')
def patient(request):
    return render(request,'patient.html')
def doctor(request):
    return render(request,'doctor.html')
def free(request):
    return render(request,'free.html')
def paid(request):
    return render(request,'paid.html')


