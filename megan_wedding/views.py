from django.shortcuts import render, redirect
from .models import NightGuest, DayGuest
from .forms import NightGuestForm, DayGuestForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def rsvp_check_guest(request):
    return render(request, 'rsvp_check_guest.html')

def rsvp_day_guest(request):
    if request.method == 'POST':
        DayGuest.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            number_adult=request.POST['number_adult'],
            number_children=request.POST['number_children'],
            message=request.POST['message'],


        )
        return redirect('info_sent')
    context = {}
    return render(request, 'rsvp_day_guest.html', context)


def rsvp_night_guest(request):
    if request.method == 'POST':
        NightGuest.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            telephone=request.POST['telephone'],
            number_adult=request.POST['number_adult'],
            number_children=request.POST['number_children'],
            message=request.POST['message'],
        )
        return redirect('info_sent')
    context = {}
    return render(request, 'rsvp_night_guest.html', context)


def imformation_sent(request):
    return render(request, 'imformation_sent.html')


def night_guest_data(request):
    NightGuests = NightGuest.objects.all()
    context = {'NightGuests': NightGuests}
    return render(request, 'admin_night_guest_data.html', context)

def day_guest_data(request):
    DayGuests = DayGuest.objects.all()
    context = {'DayGuests': DayGuests}
    return render(request, 'admin_day_guest_data.html', context)


def edit_NightGuest(request, pk):
    guest = NightGuest.objects.get(id=pk)
    form = NightGuestForm(instance=guest)
    if request.method == 'POST':
        form = NightGuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
        return redirect('night_data')
    context = {'form':form}
    return render(request, 'admin_NightGuest_edit.html', context)

def edit_dayGuest(request, pk):
    guest = DayGuest.objects.get(id=pk)
    form = DayGuestForm(instance=guest)
    if request.method == 'POST':
        form = DayGuestForm(request.POST, instance=guest)
        if form.is_valid():
            form.save()
        return redirect('day_data')
    context = {'form':form}
    return render(request, 'admin_day_guest_edit.html', context)



def delete_day(request, pk):
    day_guest = DayGuest.objects.get(id=pk)
    if request.method == 'POST':
        day_guest.delete()
        return redirect('day_data')
    return render(request, 'delete.html')


def delete_day(request, pk):
    day_guest = DayGuest.objects.get(id=pk)
    first_name = day_guest.first_name
    if request.method == 'POST':
        day_guest.delete()
        return redirect('day_data')
    context = {'day_guest':day_guest,'first_name':first_name}
    return render(request, 'admin_day_delete.html', context)


def delete_night(request, pk):
    night_guest = NightGuest.objects.get(id=pk)
    first_name = night_guest.first_name
    if request.method == 'POST':
        night_guest.delete()
        return redirect('night_data')
    context = {'night_guest':night_guest,'first_name':first_name}
    return render(request, 'admin_night_delete.html', context)