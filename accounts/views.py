from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django import forms
from django.contrib import messages

# Create your views here.


# User Login  
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'invaild !!!')
            return redirect('login')
    else:
        return render(request, 'login.html')



# user Registation
def register(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        email  = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1 == password2 :

            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name Taken !!!')
                return redirect('register')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Number is Taken !!!')
                return redirect('register')            
            else:

                user = User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                print('user Create')
                return redirect('login')

        else :
            messages.info(request,'Password  is not matching  !!!')
            return redirect('register')
        return redirect('/')

    else:
        return render(request,'registration.html')


# logout 
def logout(request):
    auth.logout(request)
    return redirect('/')

