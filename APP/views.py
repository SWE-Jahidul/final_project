from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


from .models import Notice,News,Evnets,Mayor_and_councilor,Contract

from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')


def complain(request):
    return render(request,'compalin.html')



def mayor_and_councilor(request):
    
    mayor_con = Mayor_and_councilor.objects.all()
    context = {
        "mayor_con":mayor_con
    }

    return render(request, 'mayor_and_councilor.html',context)


def notice(request):

    notice = Notice.objects.all()
    context = {
        "notice":notice
    }
    return render(request, 'notices.html',context)


def news(request):
    news_w = News.objects.all()
    context = {
        "news_w":news_w
    }
    return render(request,'news.html',context)




def events(request):
    evnet = Evnets.objects.all()
    context = {
        "evnet":evnet
    }

    return render(request,'events.html',context)


def gallary(request):
    return render(request,'gallary.html')



def contact(request):
    cont = Contract.objects.all()
    context = {
        "cont":cont
    }
    return render(request,'contact.html' ,context)



def compalin_list_chart_view(request):
    return render(request ,'compalin_list_chart_view.html')