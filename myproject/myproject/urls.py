"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings                     # ye setting.py ko lane ke liye he
from django.conf.urls.static import static           # ye funtion isliye import kiya he kyuki settings me se MEDIA_URL ko isme load karne ke liye

# is tarike se header aur title change kar sakte he iska
admin.site.site_header = "muneeb ur rehman admin" 
admin.site.site_title = "django"
admin.site.index_title = 'Site administration'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('myapp.urls')),            # ye include method kya karta he ki ye check karta settings me myapp ko agar he to uska urls.py de deta he

    
    path("__reload__/", include("django_browser_reload.urls")),   # ye hi path he jo reload ko call karta he aur ye path sabse last me likhenge kyuki ye kuch chize bhejta he to time lag sakta he
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)   # ye method batayga isko kis tarah load karna he aur isko document_root bhi batana padta he taki MEDIA_URL path pe document_root ye show ho


