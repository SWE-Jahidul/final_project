from django.contrib import admin

# Register your models here.

from .models import Notice,Mayor_and_councilor,News,Contract

# Register your models here.
admin.site.register(Notice)
admin.site.register(Mayor_and_councilor)
admin.site.register(News)
admin.site.register(Contract)
