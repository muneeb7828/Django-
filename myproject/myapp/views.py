from django.shortcuts import render,HttpResponse  # isme jo render he ye templates ko render karne ke liye he

# Create your views here.
def Index(request):
    return HttpResponse("this is homepage")       # HttpResponse ye method string ko render(dikhane) ke liye hota he
                                                  # aur ham render(dikhane) ke liye iska use nahi templates ka use karenge


def About(request):                                       # is parameter me path ka name ata he
    contex={"fname":"muneeb","lname":"ur rehman"}         # is tarike se variable daal sakte html me aur ye dict hi hona chahiye
    return render(request,'about.html',contex)            # is tarike se ham templates ko render karte he
    

def Contact(request):
    return render(request,'contact.html') 





