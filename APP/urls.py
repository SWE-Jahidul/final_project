from django.urls import path 


from . import views

from  .views import compalin_list_chart_view, get_data,ChartData

urlpatterns = [
    path('' , views.home , name ='home'),
    path('complain/', views.complain , name ='complain' ),
    path('mayor_and_councilor/' , views.mayor_and_councilor , name ='mayor_and_councilor'),
    path('notice/' , views.notice , name ='notice'),
    path('news/', views.news , name = 'news'),
    path('events/', views.events , name = 'events'),
    path('gallary/', views.gallary , name = 'gallary'),
    path('contact/',views.contact , name ='contact'),
    path('add_complain_submission/',views.add_complain_submission, name='add_complain_submission'),
  
    path('compalin_list_chart_view/',compalin_list_chart_view.as_view(), name ='compalin_list_chart_view'),
    path('api/chart/data/',ChartData.as_view()),
    path('api/data',get_data,name='api-data'),
 

]



