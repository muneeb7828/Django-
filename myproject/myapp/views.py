from django.shortcuts import render,HttpResponse  # isme jo render he ye templates ko render karne ke liye he

# Create your views here.
def Index(request):
    return HttpResponse("this is homepage")       # HttpResponse ye method string ko render(dikhane) ke liye hota he
                                                  # aur ham render(dikhane) ke liye iska use nahi templates ka use karenge


def About(request):
    return HttpResponse("this is aboutpage") 


def Contact(request):
    return HttpResponse("this is contactpage") 





