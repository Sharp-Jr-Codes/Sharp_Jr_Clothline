from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# email import
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage


def signup(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            messages.warning(request,"Password is Not Matching")
            return render(request,'signup.html')


        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return render(request,'accouts/signup.html')

        except Exception as identifier:
            pass
        
        myuser = User.objects.create_user(email,password)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        messages.info(request,"Signup SuccessFull! Please Login ")
        return redirect('accounts/login')

    return render(request,'signup.html')



def handlelogin(request):
    if request.method=="POST":

        username=request.POST['email']
        userpassword=request.POST['pass1']
        myuser=authenticate(username=username,password=userpassword)

        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Success")
            return render(request,'index.html')

        else:
            messages.error(request,"Something went wrong")
            return redirect('/login')

    return render(request,'login.html')    



def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")
    return redirect('accounts/login')