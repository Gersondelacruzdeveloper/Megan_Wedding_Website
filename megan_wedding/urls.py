from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('check_guest', views.rsvp_check_guest, name="check_guest"),
    path('day_guest', views.rsvp_day_guest, name="day_guest"),
    path('night_guest', views.rsvp_night_guest, name="night_guest"),
    path('info_sent', views.imformation_sent, name="info_sent"),
    path('night_data', views.night_guest_data, name="night_data"),
    path('day_data', views.day_guest_data, name="day_data"),
    path('edit/<str:pk>/', views.edit_NightGuest, name="edit"),
    path('edit_day/<str:pk>/', views.edit_dayGuest, name="edit_day"),
    path('day_delete/<str:pk>/', views.delete_day, name="day_delete"),
    path('night_delete/<str:pk>/', views.delete_night, name="night_delete"),
]
