from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from .models import Notice,News,Evnets,Mayor_and_councilor,Contract,Complain_details
from django.http import HttpResponse
from .models import Complain_details
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

    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    return render(request, 'home.html' ,{'toi_news':toi_news,'wdetails':wdetails,'we_temp':we_temp,'mapbox_access_token' : mapbox_access_token})


def complain(request):
    return render(request,'compalin.html')


def add_complain_submission(request):
    complainer_name = request.POST['complainer_name']
    complainer_email = request.POST['complainer_email']
    compain_location = request.POST['compain_location']
    complain_subject = request.POST['complain_subject']
    problem_details = request.POST['problem_details']


    compain_details = Complain_details(complainer_name=complainer_name,complainer_email=complainer_email,compain_location=compain_location,complain_subject=complain_subject,problem_details=problem_details)
    compain_details.save()
    return render(request,'compalin.html')

def mayor_and_councilor(request):
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    mayor_con = Mayor_and_councilor.objects.all()
    context = {
        "mayor_con":mayor_con,
         'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }

    return render(request, 'mayor_and_councilor.html',context)


def notice(request):
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    notice = Notice.objects.all()
    context = {
        "notice":notice,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }
    return render(request, 'notices.html',context)


def news(request):
    news_w = News.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    context = {
        "news_w":news_w,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }
    return render(request,'news.html',context)




def events(request):
    evnet = Evnets.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'

    context = {
        "evnet":evnet,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }
    
    return render(request, 'events.html',context) 
    



def gallary(request):
    return render(request,'gallary.html')



def contact(request):
    cont = Contract.objects.all()
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    context = {
        "cont":cont,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }
    return render(request,'contact.html' ,context)



def compalin_list_chart_view(request):
    return render(request ,'compalin_list_chart_view.html')



# Weather section start 
