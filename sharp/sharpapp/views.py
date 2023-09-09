from django.shortcuts import render, redirect
from .models import Contact,Product
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core import mail
from django.core.mail.message import EmailMessage

# Create your views here.
def index(request):
    return render(request, 'index.html')




def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphone=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phone_number=fphone,description=fdesc)
        query.save()
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_messge=mail.EmailMessage(f'Email from {fname}',f'Query : {fdesc}\nUser Email : {femail}\nPhone Number : {fphone}',from_email,['ctrl1root@gmail.com','14payload@gmail.com'],connection=connection)  
        email_client=mail.EmailMessage('Sharp',f'Hello {fname}\nGreetings of the day\n\nThanks For Visiting us will get back you soon',from_email,[femail],connection=connection)
        connection.send_messages([email_messge,email_client])
        connection.close()
        messages.success(request,"Thanks for Contacting Us")
      
        return redirect('/contact')

    return render(request,'contact.html') 

def search(request):
    query=request.GET['search']
    if len(query)>78:
        allPosts=Product.objects.none()
    else:
        allPostsTitle=Product.objects.filter(title__icontains=query)
        allPostsContent=Product.objects.filter(description__icontains=query)
        allPosts=allPostsTitle.union(allPostsContent)

    if allPosts.count()== 0:
        messages.warning(request,"No Search Results")

    params={'allPosts':allPosts,'query':query}   
     
    return render(request,'search.html',params)