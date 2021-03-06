from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

from .models import Notice,News,Evnets,Mayor_and_councilor,Contract,Complain_details
from django.http import HttpResponse
from .models import Complain_details
import requests
from bs4 import BeautifulSoup
#  paginator

from django.core.paginator import Paginator,EmptyPage
from django.contrib import messages


# for chart 

from django.views.generic import View
from django.views.generic import TemplateView
# email 
from django.conf import settings

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

from django.utils.translation import gettext as _



page = requests.get('https://www.bbc.com/weather/1185241')
soup = BeautifulSoup(page.content, 'html5lib')
# today
hedings  = soup.find_all("div",{"class": "wr-day__title"})
weather_type = soup.find_all("div",{"class": "wr-day__weather-type-description" })
weather_temperature = soup.find_all("span",{"class": "wr-value--temperature--c" })

from django.utils.translation import gettext as _




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

    from django.utils import translation
    # user_language = 'fi'
    # translation.activate(user_language)
    # request.session[translation.LANGUAGE_SESSION_KEY] =user_language
    # text = _("this is some random text")
    # if translation.LANGUAGE_SESSION_KEY in request.session:
    #     del request.session[translation.LANGUAGE_SESSION_KEY]
   
    title = _('Homepage')
    context = {
        "news_w":page,
        
    } 

    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
       
    return render(request, 'home.html',{'toi_news':toi_news,'wdetails':wdetails,'we_temp':we_temp,'mapbox_access_token' : mapbox_access_token,'title':title ,})


def complain(request):
    return render(request,'compalin.html')


def add_complain_submission(request):
    complainer_name = request.POST['complainer_name']
    complainer_email = request.POST['complainer_email']
    compain_location = request.POST['compain_location']
    complain_subject = request.POST['complain_subject']
    problem_details = request.POST['problem_details']
    # test = request.POST['test',False]


    compain_details = Complain_details(complainer_name=complainer_name,complainer_email=complainer_email,compain_location=compain_location,complain_subject=complain_subject,problem_details=problem_details,test=test)
    compain_details.save()
    return render(request,'compalin.html')

def mayor_and_councilor(request):
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    mayor_con = Mayor_and_councilor.objects.all()
    mayor_title_query_or_degination = request.GET.get('title_contains2')
    # cheack 
   

    if mayor_title_query_or_degination != '' and mayor_title_query_or_degination is not None:
        mayor_con =mayor_con.filter(Q(mayor_or_councilor_name__icontains=mayor_title_query_or_degination)|
        Q(deginaion__icontains=mayor_title_query_or_degination) ).distinct()
    else: 
        messages.info(request,"please search again")

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
    notice_title_query = request.GET.get('notice_contins')
    # cheack 
   

    if notice_title_query != '' and notice_title_query is not None:
        notice =notice.filter(heading__icontains = notice_title_query )
    else: 
        messages.info(request,"please search again")
        
    p = Paginator(notice,2) 
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page =p.page(1)
    context = {
        "notice":page,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    }
    return render(request, 'notices.html',context)

def sendanmail(request):
    if request.method == "POST":
        to= request.POST.get('toemail')
        content = request.POST.get('content')
        html_content = render_to_string("email_tamplate.html",{'title':'test email','content':content})
        text_content =strip_tags(html_content)
        # print(to,content)

        email = EmailMultiAlternatives(
            "testing",
            text_content,

            settings.EMAIL_HOST_USER,
            [to]

        )
        email.attach_alternative(html_content,"text/html")
        email.send()
        # print(to,content)

       
        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
        )
    else:  
        return render(
            request,
            'email.html',
            {
                'title': 'send an email'
            }
   )



def news(request):
    news_w = News.objects.all().order_by("-id")
    # search News 
    news_title_query = request.GET.get('title_contains')
    # cheack 
   
    if news_title_query != '' and news_title_query is not None:
        news_w =news_w.filter(news_title__icontains = news_title_query )
    else: 
        messages.info(request,"please search again")
        
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    p = Paginator(news_w,2) 
    page_num = request.GET.get('page',1)
    try:
        page = p.page(page_num)
    except EmptyPage:
        page =p.page(1)
    context = {
        "news_w":page,
        'toi_news':toi_news,
        'wdetails':wdetails,
        'we_temp':we_temp,
        'mapbox_access_token' : mapbox_access_token,
    } 
    return render(request,'news.html',context)




def events(request):
    evnet = Evnets.objects.all().order_by("-e_date")
    mapbox_access_token = 'pk.eyJ1IjoiamFoaWR1bDciLCJhIjoiY2tmZHAxODAzMDY1cjJ6cDV6a3o2N25qcSJ9.mcQR9Z0kZ2AqEYm3Q_9sVg'
    event_title_query = request.GET.get('title_contains1')
    # cheack 
   

    if event_title_query != '' and event_title_query is not None:
        evnet =evnet.filter(Events_title__icontains = event_title_query )
    else: 
        messages.info(request,"please search again")
   
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



User = get_user_model()


class compalin_list_chart_view(View):
    def get(self, request, *args, **kwargs):
        return render(request ,'compalin_list_chart_view.html',{"customers": 10})



def get_data(request,*args, **kwargs):
    data ={
        "sales":100,
        "customers":10,
        
    }
    
    return JsonResponse(data)



 
class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
     
        qs_count = Complain_details.objects.all().count()
        water_count = Complain_details.objects.filter(problem_categories='water').count()
        traffic_count = Complain_details.objects.filter(problem_categories='traffic').count()
        loadshedding_count = Complain_details.objects.filter(problem_categories='loadshaading').count()
        dirty_count = Complain_details.objects.filter(problem_categories='dirtyproblem').count()
        air_polution_count = Complain_details.objects.filter(problem_categories='airPolution').count()
        labels =['Water', 'Traffic',  'Load Shedding', 'Darty Problem ', 'Air Pollution']
        default_items = [water_count,traffic_count,loadshedding_count,dirty_count,air_polution_count]
        data ={
                 "labels":labels,
                 "default":default_items,
             
            }
        return Response(data)

