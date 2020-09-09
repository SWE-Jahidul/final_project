from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth



from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')


# def login(request):
#     return render(request, 'login.html')


# def registration(request):
#         return render(request, 'registration.html')


def complain(request):
    return render(request,'compalin.html')



def mayor_and_councilor(request):
    return render(request, 'mayor_and_councilor.html')


def notice(request):
    return render(request, 'notices.html')



def news(request):
    return render(request,'news.html')




