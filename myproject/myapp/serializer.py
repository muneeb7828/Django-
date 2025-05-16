from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields=['id','name','rollno','city']                      # yaha jo bhi field likhenge ye bas unko hi json format me convert karke dega






