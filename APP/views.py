from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth


from .models import Notice,News,Evnets,Mayor_and_councilor,Contract

from django.http import HttpResponse


import requests
from bs4 import BeautifulSoup

# Create your views here.



page = requests.get('https://www.bbc.com/weather/1185241')
soup = BeautifulSoup(page.content, 'html5lib')
# today
hedings  = soup.find_all("div",{"class": "wr-day__title"})
weather_type = soup.find_all("div",{"class": "wr-day__weather-type-description" })
weather_temperature = soup.find_all("span",{"class": "wr-value--temperature--c" })



hedings = hedings[0:-13]
weather_type = weather_type[0:-13]
weather_temperature = weather_temperature[ 0: 1]

toi_news = []
wdetails =[]
we_temp = []

for th in hedings:
    toi_news.append(th.text)

for wd in weather_type:
    wdetails.append(wd.text)

for wt in weather_temperature:
    we_temp.append(wt.text)


# The Next Day 


def home(request):
    return render(request, 'home.html' ,{'toi_news':toi_news,'wdetails':wdetails,'we_temp':we_temp,})


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



# Weather section start 
