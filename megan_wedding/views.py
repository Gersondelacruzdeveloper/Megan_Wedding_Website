from django.shortcuts import render, redirect
from .models import NightGuest, DayGuest
from .forms import NightGuestForm, DayGuestForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url= 'login')
def home(request):
    return render(request, 'home.html')

@login_required(login_url= 'login')
def contact(request):
    return render(request, 'contact.html')
@login_required(login_url= 'login')
def events(request):
    return render(request, 'events.html')

@login_required(login_url= 'login')
def rsvp_check_guest(request):
    return render(request, 'rsvp_check_guest.html')

@login_required(login_url= 'login')
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

@login_required(login_url= 'login')
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

@login_required(login_url= 'login')
def imformation_sent(request):
    return render(request, 'imformation_sent.html')

@login_required(login_url= 'login')
def night_guest_data(request):
    NightGuests = NightGuest.objects.all()
    context = {'NightGuests': NightGuests}
    return render(request, 'admin_night_guest_data.html', context)
@login_required(login_url= 'login')
def day_guest_data(request):
    DayGuests = DayGuest.objects.all()
    context = {'DayGuests': DayGuests}
    return render(request, 'admin_day_guest_data.html', context)

@login_required(login_url= 'login')
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
@login_required(login_url= 'login')
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


@login_required(login_url= 'login')
def delete_day(request, pk):
    day_guest = DayGuest.objects.get(id=pk)
    if request.method == 'POST':
        day_guest.delete()
        return redirect('day_data')
    return render(request, 'delete.html')

@login_required(login_url= 'login')
def delete_day(request, pk):
    day_guest = DayGuest.objects.get(id=pk)
    first_name = day_guest.first_name
    if request.method == 'POST':
        day_guest.delete()
        return redirect('day_data')
    context = {'day_guest':day_guest,'first_name':first_name}
    return render(request, 'admin_day_delete.html', context)

@login_required(login_url= 'login')
def delete_night(request, pk):
    night_guest = NightGuest.objects.get(id=pk)
    first_name = night_guest.first_name
    if request.method == 'POST':
        night_guest.delete()
        return redirect('night_data')
    context = {'night_guest':night_guest,'first_name':first_name}
    return render(request, 'admin_night_delete.html', context)

@login_required(login_url= 'login')
def acomodation(request):
    context = {}
    return render(request, 'acomodation.html', context)