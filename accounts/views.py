from django.shortcuts import render,redirect
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request,'accounts/home.html')
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials")
            return redirect("login")
    else:
        return render(request,"accounts/login.html")

def register(request):
    if request.method=="POST":
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        phonenumber=request.POST['phonenumber']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email taken")
                return redirect("register")
            else:
                user=User.objects.Create_user(firstname=firstname,lastname=lastname,phonenumber=phonenumber,email=email,username=username,password=password,confirm_password=confirm_password)
                user.save()
                print("user created")
                return redirect("login")
        else:
            messages.info(request,"password not matching")
            return redirect("register")
        return redirect("/")
    else:
        return render(request,"accounts/registration.html")
def logout(request):
    auth.logout(request)
    return redirect('/')