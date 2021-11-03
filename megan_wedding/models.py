from django.db import models

# Create your models here.

class NightGuest(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    number_adult = models.IntegerField(blank=True, null=True)
    number_children = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.first_name)

class DayGuest(models.Model):
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=200, blank=True, null=True)
    number_adult = models.IntegerField(blank=True, null=True)
    number_children = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.first_name)
