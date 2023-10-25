from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class signup(models.Model):
    Firstname=models.CharField(max_length=50) 
    Lastname=models.CharField(max_length=50)
    Mobile_Number=models.BigIntegerField()
    
    DOB=models.CharField(max_length=20)
    Gender=models.CharField(max_length=10)
class login(models.Model):
    Email=models.EmailField(max_length=250)
    Password=models.CharField(max_length=20) 
    user_id=models.ForeignKey(signup,on_delete=CASCADE,default=None)   
