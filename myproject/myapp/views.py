from django.shortcuts import render,HttpResponse  # isme jo render he ye templates ko render karne ke liye he
from datetime import datetime
from myapp.models import Contact                              # isse sab import ho jate he

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
    if (request.method == "POST"):      # ye POST '/contact' return karta he
        name=request.POST.get("name")
        email=request.POST.get("email")
        phone=request.POST.get("phonenumber")
        desc=request.POST.get("desc")
        date=datetime.today()
        print(name,email,phone)
        cntact=Contact(name=name,email=email,phone=phone,desc=desc,date=date)    # ye instance bana raha he jab bhi submit pe click ho raha he
        cntact.save()                                        # ye save kar deta he instance ko database me
    return render(request,'contact.html')
    



