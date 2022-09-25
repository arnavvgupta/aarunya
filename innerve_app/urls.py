from django.contrib import admin
from django.urls import path
from innerve_app import views

urlpatterns = [
    path('',views.index,name="home"),
    path('choose',views.choose,name="choose"),
    path('doctor',views.doctor,name="doctor"),
    path('patient',views.patient,name="patient"),
    path('free',views.free,name="free"),
    path('paid',views.paid,name="paid"),

]