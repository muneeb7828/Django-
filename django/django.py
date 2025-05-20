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
# python manage.py makemigrations     # ye changes ko store karleta he file me
# python manage.py migrate            # ye jo makemigrations se save hua he usko database me save kar deta he 
# python manage.py  createsuperuser   # is command se user ka username email password set kar sakte he
# python manage.py changepassword <user>
# python manage.py runserver   # ye server ko start karne ke liye hoti he 
# python manage.py shell       # isse djangp ki command terminal pe chala sakte he
# python -m pip install Pillow  # ye module he imagefield ke liye

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
    # 'rest_framework',
    # 'myapp',
# ]

# DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME':'project',
    #     'USER':'root',
    #     'PASSWORD':'Muneebmysql@12345',
    #     'HOST':'localhost',
    #     'PORT':'3306'
    # }
# }

# django html me agar html ke emmet use karna he to setting me jage emmet likhna he fir include language me item me django-html aur value me html likhna he


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
# aur css javascript bhi static folder me banate he

# templates
# setting.py is file me TEMPLATES ke DIRS iske andar agar ye BASE_DIR / "template" likhenge to template ki files ko bhi use kar payenge 
# aur templates kahin bhi bana sakte he

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
# aur ye he iska syntax {% block title %} default value {% endblock title %} 

# for loop block
# {% for message in messages %}  {% endfor %}

# if else block
# {% if messages %} {% endif %}

# tailwind in django

# pip install django-tailwind
# pip install 'django-tailwind[reload]'
# after that we need to add tailwind in settings.py INSTALLED_APPS 
# python manage.py tailwind init and add this command in child myproject aur isse ek theme folder milega aur isko bhi add karna padega settings.py INSTALLED_APPS isme
# aur iske baad ek variable banana padega tailwind app ka name batene ke liye 'TAILWIND_APP_NAME'='theme' aur isi ke sath sath ek aur variable banana padega internal ip batane ke liye kyuke 2 server ek sath jod rahe he 'INTERNAL_IPS'=['127.0.0.1']  
# aur iske baad python manage.py tailwind install ye command likhenge agar ye command nahi chali to NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd" ye command likhenge taki django detake karle npm ko
# aur ye karne ke baad tailwind install hojayga lekin abhi bhi nahi chalega isko generate bhi karna padega naya terminal open karke 
# fir ye command use karenge tailwind ko start karne ke liye python manage.py tailwind start fir uske baad fir se run server ko start karna padega fir ab isko use kar sakte he


# isko use karne ke liye theme ke base.html me 2 blocks hote he {% load static tailwind_tags %} aur {% tailwind_css %} to jaha bhi tailwind use waha ye dono blocks likhna padega 

# auto reload in django
# jo hamne reload install kiya he isko bhi add karna hoga settings.py INSTALLED_APPS isme is name se 'django_browser_reload' aur settings.py middleware me 'django_browser_reload.middleware.BrowserReloadMiddleware' ye add karna hoga
# fir uske baad myproject ke urls.py me sabse niche ye path add karna hoga path("__reload__/", include("django_browser_reload.urls")) kyuki ye hi reload ko call karega
# aur production me ye use nahi karenge waha build hota he jo apne aap call kar deta he



# django rest framework

# ye ham isliye learn kar rahe he taki hame api's banani he aur banake frontend ko data bhejna he aur frontend react ho sakta ya kuch aur bhi

# serializer in django
# complex datatype (table) ko python datatype me convert karna fir usko json format me convert karne ko serialization bolte he

# de-serializer in django
# iski zarurat tab padti he jab object (data) ko database me add karna ho ya delete karna ho ya update karna ho
# serializer isi ko opposite dardo to de-serializer bolte he yani json se python datatype fir complex datatype me convert karne ko bolte he

# nested serializer
# nested serializer matlab ek serializer me dusre serializer ko use karna yani 2 table he usme ek table dusre table se reference le rahi he to jo reference le rahi uska data bhi parent table me dikhane ko hi nested serializer bolte he
# aur nested serializer bydefault read only hota he

# stream



# User in django
# jab bhi user banate he to admin panel pe staff status no show hota he iska matlab vo admin panel login nahi kar sakta aur superuser status no show ho to vo admin panel pe kuch bhi nahi dekh sakta
# bas superuser hi dekh sakta he

# bad request
# bad request tab aati jab object banane me khuch galti kari ho to json.parse me convert nahi ho pata

# from django.contrib.auth.models import User    # isse  jo admin pe user hota he vo import vo import ho jata he
# is User me jitne bhi user bane hote he vo sab user ke object (data) ajate he matlab ke ye jo User he ye database hi he jese Course model database he jisme sare object (data) hote he

# from django.contrib.auth import authenticate,login,logout   # ye function user ko authenticate karne ke liye aur login or logout karne ke liye hota he
# aur ye dono views me hi import karte he

# login logout signup of user
# teeno case me post method use hoga kyuke teeno me hi khuch bhej rahe he

# isme jo username hota he isko kese bhi get kar sakte he kyuki ye case insensitive hota he u
# jis bhi project se model banate he usi se kholte he to models show hote he


# class base view set
# isi me model view set hota he

# model view set
# ye aur asaan kar deta he database me data ko crud karna isme funtion ki jagah class ka us hota he aur isme sare views ek single class me rakhe jate he isi ko view set bolte he
# aur isme alag agal url banane ki zarurat nahi padti isme router hota he agar usme class define kardi to url ka kaam router hi karlega
# aur viewset  method get post aur bhi provide nahi karta ye actions provide karta he jiske andar list() get all records, create() create record, retrieve() get single record, update() update record, partial_update() update record partially, destroy() delete record, ye sab hote he jo ke method ka hi kaam karte he
# from rest_framework import viewsets 
# from rest_framework.routers import DefaultRouter    ye hi router banata he
# aur jab bhi class banate he to viewsets.ViewSet is class ko inherit karna padta he
# aur jab bhi viewset class banate he to isme basename,action,detail, ye attributes hote he
# basename ye batata he jo bhi url name dete he
# action ye konsa operation ho raha he list ho rahe ya create ho raha he
# detail ye bolean return karta he


# public private key criptography
# isme 2 keys generate hoti he public key aur private key
# public key
# public key isko kisi ko bhi bata sakte lekin isse jo data aayga vo private key se milke hi aayga
# priavte key 
# priavte key iski information bas apan ko pata honi chahiye

# state less and state full
# state less iski information ham database me ya file me store karke nahi rakhte exp http ye stateless mechanisym pe work karta he 
# state full iski information database aur file me store hoti he

# Encryption and decryption
# Encryption is the process of converting readable data (plaintext) into an unreadable format (ciphertext), while decryption is the reverse process, converting ciphertext back into plaintext

# JWT (json web token) authentication
# JWT ye bhi public private criptography ki tarah kaam karta he aur state less hota he
# isme kya hota he isme token generate hota to jiske paas bhi token hota he vo authenticate kar sakta he
# jwt me kya hota he ye aapka data leta he usko encript kar dete he aur kon decript karega ye server decide karega
# iske token me 3 parts hote he 1 part me kya hota he ki ye batata he konsi algoritym use kar rahe he kyuke isme bohot sare algoritym hoti he 2 part batata he ki kya informtion he aapke paas me 3 part signature hota he ye check karta he ki data me kuch change to nahi he
# authentication and authorization in dono ye different hota he authentication matlab varify karna aur authorization matlab kisi cheez ko access kar pana
# aur isme har token ke sath expiry time bhi dal sakte he ki kab token expire hoga

















# download postman






