from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200,default='') 
    heading = models.CharField(max_length=150,default='') 
    Notice_decription =  models.TextField(max_length=1024*3, default='')
    notice_date = models.DateTimeField(auto_now_add=True ) 
    
    def __str__(self):
        return self.title



class Mayor_and_councilor(models.Model):
    mayor_or_councilor_image = models.ImageField(upload_to='images')
    mayor_or_councilor_name = models.CharField(max_length=150 ,default='') 
    deginaion = models.CharField(max_length=100 ,default='') 
    email = models.CharField(max_length=150 ,default='') 
    about = models.CharField(max_length=250,default='')
    def __str__(self):
        return self.mayor_or_councilor_name



class News(models.Model):
    news_images =models.ImageField(upload_to='images')
    news_title = models.CharField(max_length=150, default='') 
    news_details = models.CharField(max_length=1024*3 , default='')
    news_date = models.DateTimeField(auto_now_add=True )

    def __str__(self):
            return self.news_title

    
    
class Contract(models.Model):
    contact_number_title =  models.CharField(max_length=150,default='')
    phone_number = models.IntegerField()

    def __str__(self):
        return self.contact_number_title


class Evnets(models.Model):
    
    Events_images = models.ImageField(upload_to='images')
    Events_title = models.CharField(max_length=150,default='')
    e_time = models.CharField(max_length=150,default='')
    e_date = models.CharField(max_length=150,default='')
    Ecent_location =models.CharField(max_length=150,default='')


    def __str__(self):
        return self.Events_title



class Complain_details(models.Model):

    
    PROBLEMS_CATEGORIES = (
        ("traffic", "Traffic"),
        ("water", "Water"),
        ("loadshaading", "Load Shaading"),
        ("dirtyproblem", "Dirty Problem"),
        ("airPolution", "Air Polution"),
    )

    complainer_name = models.CharField(max_length=50,default='')
    complainer_email = models.CharField(max_length=30,default='')
    compain_location = models.CharField(max_length=100,default='')
    complain_subject = models.CharField(max_length=100,default='')
    problem_details = models.CharField(max_length=250,default='')
    problem_categories = models.CharField(max_length=20, choices=PROBLEMS_CATEGORIES, default="water")

    def __str__(self):
        return self.complainer_name
