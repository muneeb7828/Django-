# what is django

# django ek framework he jo website banane ko aur asaan kar deta he
# aur ye modules deta he jisme html css ye sab likhi he to baar baar likhna nahi padta
# aur iske andar database connector hota he
# aur iske andar url dispatcher hota he jo ki alag alag page ko dikha neme madad karta he aur alag alag views ko bhi manage karta he
# aur isme project ek hota he lekin apps bohot sare bana sakte he
# aur django default authentication system ke sath ata he is liye ham django ko use karte he


# mvt architecture of django

# ye mvc architecture ki tarah hota he jo ki bohot famaous he
# ye softwaredesign pattern he (model view template)

# model
# model ye database banata he

# view
# view ye template se associated hota he aur ye runtime par model se data pull karta he aur pull karne ke baad processing karta he aur ye karne ke baad ye data template ko bhej dega


# template
# ye ui hota he aur jab bhi kuch event hota he to ye view ko chalata he aur waha se jo ata he ye usko dikhata he



# commands to install for django

# pip install mysqlclient
# pip install django
# pip install djangoclient
# pip install Djangorestframework
# pip show django

# command for create project
# python -m django startproject myproject
# django-admin startproject myproject

# command for create app
# python -m django startapp myapp1

# commands after go to myproject
# python manage.py makemigrations     # ye check karta he kuch change hua database me ke nahi
# python manage.py migrate
# python manage.py  createsuperuser   # is command se user ka username email password set kar sakte he
# python manage.py runserver   # ye server ko start karne ke liye hoti he 

# extentions in django
# django
# thunder client

# myproject setting.py

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     'rest_framework',
#     'myapp',
# ]

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME':'project',
#         'USER':'root',
#         'PASSWORD':'Muneebmysql@12345',
#         'HOST':'localhost',
#         'PORT':'3306'
#     }
# }


# project and app in django 
# aur isme project ek hota he lekin apps bohot sare bana sakte he
# aur project aur app kisi bhi naam se bana sakte he
# aur project me ek setting.py file hoti aur ye project ke specifications ke liye hoti he
# aur project me urls.py file hoti aur app me nahi hoti to app me banani padti he


# aur django me url add karne ke liye project ke urls.py ko edit karna padta he
# aur jab bhi koi request hoti he to phele project ke urls.py me aati he fir vo kisi app ke url.py me jati he


# aur ham myproject me 2 folder banayenge templates aur static

# static
# isme saari static files ayengi aur static files images aur dusri files ke liye hoti he 
# jo koi bhi aapke server pe aake dekh sakta he
# is tarike se kisi bhi static file ko get kar sakte he  <img src="static/image.jpg" alt="">

# templates
# setting.py is file me TEMPLATES ke DIRS iske andar agar ye BASE_DIR / "template" likhenge to template ki files ko bhi use kar payenge 


# templates inheritance
# agar ek page ke component ko dusre page ke component ke sath dikhana chahte he to iska use karenge
# isme hota he extends and block body and block title

# extends
# ye tab use karte he jab bhi kisi component ko inherit karna ho to aur ye he iska syntax {% extends 'base.html' %}

# block body
# ye tab use karte he jab inherit karne ke baad kuch karna ho to isme karenge aur isko parent html me bhi likhte he position ke liye 
# aur ye he iska syntax {% block body %} {% endblock body %}

# block title
# ye bhi block body ki tarah hota he bas ye title ke andar use hota he
# aur ye he iska syntax {% block title %} {% endblock title %} 













