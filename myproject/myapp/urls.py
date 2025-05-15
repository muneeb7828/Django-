
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('',views.Home,name="home"),                     # jo name diya he ye batata he pure path ka name kya he
    path('about',views.About,name="about"),
    path('contact',views.contact,name="contact"),
    path('index',views.Index2,name="index"),
    path('chais',views.all_chais,name="chais"),
    # path('services',views.services,name="services"),   # ye nahi chalega taki is naam ka function nahi he

]












