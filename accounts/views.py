from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django import forms
from django.contrib import messages

# Create your views here.
# User Registration 
def register(request):
    if request.method == 'POST':
       
        username = request.POST['username']
        phone  = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
       
        if password1 == password2 :

            if User.objects.filter(username=username).exists():
                messages.info(request,'User Name Taken !!!')
                return redirect('register')
            
            elif User.objects.filter(phone=phone).exists():
                messages.info(request,'Phone Number is Taken !!!')
                return redirect('register')            
            else:

                user = User.objects.create_user(username=username)
                user.save()
                print('user Create')

        else :
            messages.info(request, 'password not matching !!!')
            return redirect('register')

    else:
        return render(request,'registration.html')




