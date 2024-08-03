from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login as authlogin,logout as authlogout,authenticate
# Create your views here.
def logout(request):
    authlogout(request)
    return redirect('login')
def login(request):
    
    errormsg=None
    if(request.POST):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if user:
            print(user)
            authlogin(request,user)
            return redirect('list')

        else:
            errormsg="invalid credentials"
            print(errormsg)
    return render(request,'user/login.html',{"error":errormsg})

def signup(request):
    user=None
    errormsg=None
    if(request.POST):
        
        username=request.POST['username']
        password=request.POST['password']
        
        try:
            user=User.objects.create_user(username=username,password=password)
        except Exception as e:
            errormsg=str(e)
    return render(request,'user/signup.html',{'user':user,'error':errormsg})