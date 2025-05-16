from django.shortcuts import render,HttpResponse  # isme jo render he ye templates ko render karne ke liye he
from rest_framework.response import Response
from datetime import datetime
from myapp.models import Contact 
from django.contrib import messages
from .models import ChaiVarity
from .models import Student
from .serializer import *                                      # isse sab import ho jate he
from rest_framework import viewsets 
from rest_framework import status

# Create your views here.


def Index(request):
    return HttpResponse("this is homepage")       # HttpResponse ye method string ko render(dikhane) ke liye hota he
                                                  # aur ham render(dikhane) ke liye iska use nahi templates ka use karenge

def Home(request):
    return render(request,'home.html') 

def Index2(request):
    return render(request,'index.html') 

def About(request):                                       # is parameter me path ka name ata he
    contex={"fname":"muneeb","lname":"ur rehman"}         # is tarike se variable daal sakte html me aur ye dict hi hona chahiye
    return render(request,'about.html',contex)            # is tarike se ham templates ko render karte he
    

def contact(request):
    print(request.method,"muneeb")                          # ye bydefault get rahega jab tak button pe click nahi karenge aur ek baar click karne ke baad bhi refresh karle to bhi post hi rahega jab wapas se page pe nahi aate aur ye bas form me hi kaam karta he
    if (request.method == "POST"):                          # ye POST '/contact' return karta he
        name=request.POST.get("name")                       # ye pura object return karta he jitne bhi name he un sab ka
        email=request.POST.get("email")
        phone=request.POST.get("phonenumber")
        desc=request.POST.get("desc")
        date=datetime.today()
        cntact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)    # ye instance bana raha he jab bhi submit pe click ho raha he
        cntact.save()                                        # ye save kar deta he instance ko database me
        messages.success(request, "your message has been send")       # this is for alert
        messages.success(request, "your message has been send succesfully")
    return render(request,'contact.html')
    



def all_chais(request):
    chais=ChaiVarity.objects.all()
    print(chais,'muneeb')
    return render(request,'chais.html',{'chais':chais})

def chais_description(request,id):                 # this is how we create dynamic page for single object (data)
    chai=ChaiVarity.objects.filter(id=id)            
    print(chai,'muneeb')
    if chai.exists():
        return render(request,'chai.html',{'chai':chai[0]})     # ye list return kar raha he isliye ese kiye he
    

# viewset

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all()
        serializer = StudentSerializer(stu,many=True)
        return Response(serializer.data)


    def retrieve(self,request,pk=None):                          # pk primary key
        id= pk
        if id is not None:
          stu=Student.objects.get(id=id)
          serializer = StudentSerializer(stu)
          return Response(serializer.data)


    def create(self,request):
        serializer = StudentSerializer(data=request.data)           # iske funtion me kwags he isliye esa likha he
        if serializer.is_valid():
            serializer.save()    
            return Response({'msg':'data created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def update(self,request,pk):
        id =pk
        stu=Student.objects.get(pk=id)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        stu=Student.objects.get(pk=pk)
        stu.delete()
        return Response({'msg':'data deleted'})
    
