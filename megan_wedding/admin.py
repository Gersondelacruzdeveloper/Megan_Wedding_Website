from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import NightGuest, DayGuest
# Register your models here.
admin.site.register(DayGuest)
admin.site.register(NightGuest)