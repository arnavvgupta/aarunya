from django.shortcuts import render,HttpResponse

def index(request):
    return render(request,'first.html')
def choose(request):
    return render(request,'first.html')
def patient(request):
    return render(request,'patient.html')
    # if request.method=="POST":
    #     # Get the post parameters
    #     username=request.POST['username']
    #     email=request.POST['email']
    #     fname=request.POST['fname']
    #     lname=request.POST['lname']
    #     pass1=request.POST['pass1']
    #     pass2=request.POST['pass2']

    #     # check for errorneous input
    #     if len(username)>10:
    #         messages.error(request, " Your user name must be less than 10 characters")
    #         return redirect('home')

    #     if not username.isalnum():
    #         messages.error(request, " User name should only contain letters and numbers")
    #         return redirect('home')
    #     if (pass1!= pass2):
    #          messages.error(request, " Passwords do not match")
    #          return redirect('home')
        
    #     # Create the user
    #     myuser = User.objects.create_user(username, email, pass1)
    #     myuser.first_name= fname
    #     myuser.last_name= lname
    #     myuser.save()
    #     messages.success(request, " Your iCoder has been successfully created")
    #     return redirect('home')

    # else:
    #     return HttpResponse("404 - Not found")


def doctor(request):
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


