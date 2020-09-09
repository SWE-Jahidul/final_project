from django.urls import path 


from . import views 

urlpatterns = [
    path('' , views.home , name ='home'),
    path('login/', views.login , name = 'login'),
    # path('registration/', views.registration , name ='registration'),
    path('complain/', views.complain , name ='complain' ),
    path('mayor_and_councilor/' , views.mayor_and_councilor , name ='mayor_and_councilor'),
    path('notice/' , views.notice , name ='notice'),

]
