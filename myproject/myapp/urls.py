
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home,name="home"),
    path('about',views.About,name="about"),
    path('contact',views.Contact,name="contact"),
    # path('services',views.services,name="services"),   # ye nahi chalega taki is naam ka function nahi he

]












