from django.db import models
from django.utils import timezone

# Create your models here.
# yahan table create karte he

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)


class Contact(models.Model):
    name= models.CharField(max_length=120)
    email= models.CharField(max_length=120)
    phone=models.CharField(max_length=12)
    desc=models.TextField()       # iske sath integer field bhi use kar sakte he aur ye compulsary field hoti he aur isme default="" bhi de sakte he
    date=models.DateField()


    def __str__(self):
        return self.name
    


class ChaiVarity(models.Model):
    Chai_type_choice=[
    ['ML','MASALA'],['GR','GINGER'],['KW','KIWI'],['PL','PLAIN'],['EL','ELAICHI']      # choices must be a mapping of actual values to human readable names or an iterable containing (actual value, human readable name)
    ]

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chaifolder/')             # ye constraint batata he jo images hongi vo kis folder me rakhi jayengi
    date_added=models.DateTimeField(default=timezone.now)        # ye default isliye diya he taki jab bhi model add ho to abhi ka time add ho
    Type=models.CharField(max_length=2,choices=Chai_type_choice) # yaha jo max length he phele index ke liye he
    description=models.TextField(default="")


    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField()
    city=models.CharField(max_length=100)

    def __str__(self):
      return self.name
  














