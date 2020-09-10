from django.db import models

# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200,default='') 
    heading = models.CharField(max_length=150,default='') 
    Notice_decription =  models.TextField(max_length=1024*3, default='')
    notice_date = models.DateTimeField(auto_now_add=True ) 
    
    def __str__(self):
        return self.title



class Mayor_and_councilor(models.Model):
    mayor_or_councilor_image =models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    mayor_or_councilor_name = models.CharField(max_length=150,default='') 
    deginaion = models.CharField(max_length=100,default='') 
    email = models.CharField(max_length=150,default='') 
    about = models.CharField(max_length=250,default='')

    def __str__(self):
        return self.mayor_or_councilor_name





class News(models.Model):
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
    
    Events_images = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    Events_title = models.CharField(max_length=150,default='')
    Events_time = models.DateTimeField(auto_now_add=True ) 
    Ecent_location = models.CharField(max_length=200,default='')


