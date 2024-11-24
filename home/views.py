from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from .models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from blog.models import Blog
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-views_count')
    blogs = blogs[:3]
    context = {'allPosts':blogs}
    return render(request,'home/index.html',context)

@csrf_exempt
def contact(request):
    if request.method=="POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        if len(name)<2 and len(email)<3 and  len(phone)<10 and len(content)<10:
            messages.error(request, "Please filled detials correctly")
        else:
            messages.success(request,"Your quries submitted !")
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

@csrf_exempt                        
def signUphandle(request):
    if request.method=='POST':
        username = request.POST.get('username')
        name = request.POST.get('name')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
    
        # check username
        if len(username)>15:
            messages.error(request,'username must be less than 15 charcters')
            return redirect('/')
        

        # username must be alphanumeric 
        if not username.isalnum():
            messages.error(request,'username should be numbers and letters')
            return redirect('/')
        
        # if pass1 not mathces pass2 
        if pass1 != pass2:
            messages.error(request,'password do not match')
            return redirect('/')
        # crate user
        user = User.objects.create_user(username,email,pass1)
        user.first_name = name
        user.last_name = lname
        user.save()
        messages.success(request,'your account crated! please login now')
        return redirect('/')
    else:
        return HttpResponse('404 not found')
    
@csrf_exempt
def logInhandle(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']

        user = authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            login(request,user)
            messages.success(request,"logged in successfully!")
            return redirect('/')
        else:
            messages.error(request,'Invalid credentials! Please try again to log in ')
            return redirect('/')
    
    return HttpResponse('404 not found')

def logOuthandle(request):
    logout(request)
    messages.success(request,'Log out successfully!')
    return redirect('/')
