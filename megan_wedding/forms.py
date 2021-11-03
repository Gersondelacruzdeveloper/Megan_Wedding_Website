from django.forms import ModelForm
from django import forms
from .models import NightGuest, DayGuest

class NightGuestForm(ModelForm):
    class Meta:
        model = NightGuest
        fields = "__all__"

class DayGuestForm(ModelForm):
    class Meta:
        model = DayGuest
        fields = "__all__"