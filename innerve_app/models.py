from unicodedata import category
from django.db import models

# Create your models here.
class Patient(models.Model):
    # sno= models.AutoField(primary_key=True)
     pname= models.CharField(max_length=255)
     email= models.CharField(max_length=100)
     dob= models.DateField(auto_now_add=True)
     pf=models.TextField(null=True)
     bg=models.CharField(max_length=13)
     content= models.TextField()
     extra= models.TextField()
     password= models.TextField(null=True)

     def __str__(self):                  # In Python, __str__ function is used to return the string representation of the object.
         return "Message from " + self.pname + ' - ' + self.email 

class Doctor(models.Model):
    # sno= models.AutoField(primary_key=True)
     dname= models.CharField(max_length=255)
     email= models.CharField(max_length=100)
     dob= models.DateField(null=False)
     phone=models.IntegerField(null=True)
     profile=models.CharField(max_length=23)
     category= models.CharField(max_length=100)
     qualification= models.CharField(max_length=100)
     fee= models.CharField(max_length=100)
    #  password1= models.TextField()
    # timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

     def __str__(self):                  # In Python, __str__ function is used to return the string representation of the object.
         return "Message from " + self.dname + ' - ' + self.email 