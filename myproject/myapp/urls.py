
from django.contrib import admin
from django.urls import path,include
from myapp import views
from rest_framework.routers import DefaultRouter     # ye router create karta he

# creating router object
router=DefaultRouter()

# register StudentViewSet with Router
router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('',views.Home,name="home"),                     # jo name diya he ye batata he pure path ka name kya he
    path('about',views.About,name="about"),
    path('contact',views.contact,name="contact"),
    path('index',views.Index2,name="index"),
    path('chais',views.all_chais,name="chais"),
    path('chais/<int:id>',views.chais_description,name="chai"),
    path('api',include(router.urls)),                    # ab isse django ko pata chal jayga router ko kaha par dikhana he
    # path('services',views.services,name="services"),   # ye nahi chalega taki is naam ka function nahi he

]












