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
    path('login',views.login,name="login"),
    path('bot',views.bot,name="bot"),
    path('logindoc',views.logindoc,name="logindoc"),
    path('mainpage',views.login,name="mainpage"),
    path('mainpagedoc',views.logindoc,name="mainpagedoc")

]