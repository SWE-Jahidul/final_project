from django.urls import path 


from . import views 

urlpatterns = [
    path('' , views.home , name ='home'),
    path('complain/', views.complain , name ='complain' ),
    path('mayor_and_councilor/' , views.mayor_and_councilor , name ='mayor_and_councilor'),
    path('notice/' , views.notice , name ='notice'),
    path('news/', views.news , name = 'news'),
    path('events/', views.events , name = 'events'),
    path('gallary/', views.gallary , name = 'gallary'),
    path('contact/',views.contact , name ='contact'),
    path('compalin_list_chart_view/',views.compalin_list_chart_view , name ='compalin_list_chart_view'),
    path('add_complain_submission/',views.add_complain_submission, name='add_complain_submission'),
 
 

]



