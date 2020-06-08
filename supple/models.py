from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Registration(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(default="null")
    username=models.CharField(max_length=20)
    mobilenumber=models.CharField(max_length=10,default="null")
    password1=models.CharField(max_length=20 ,default="null")
    password2=models.CharField(max_length=20 ,default="null")
    address = models.CharField(max_length=20, default="null")


    


class supplementsOrdered(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    onwhey = models.IntegerField(default=0)
    pro = models.IntegerField(default=0)
    mbgold = models.IntegerField(default=0)
    mpwhey = models.IntegerField(default=0)
    rcking = models.IntegerField(default=0)
    mtmass = models.IntegerField(default=0)
    syntha = models.IntegerField(default=0)
    onmass = models.IntegerField(default=0)
    onbcaa = models.IntegerField(default=0)
    mbmulti = models.IntegerField(default=0)
    mpcreatine = models.IntegerField(default=0)
    glutamine = models.IntegerField(default=0)
    asitis = models.IntegerField(default=0)
    onshaker = models.IntegerField(default=0)
    gymeq = models.IntegerField(default=0)
    gymbag = models.IntegerField(default=0)
    totalSum = models.BigIntegerField(default=0)
   
   
def __str__(self):     
   return str(self.user)
   
    

class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200,default="null")
    message = models.CharField(max_length=2000, default="null")
    

def __str__(self):
        return self.name


class Ask(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=200, default="null")
    message = models.CharField(max_length=2000, default="null")

    def __str__(self):
            return self.name



class Shipping(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField(default="null")
    username=models.CharField(max_length=20)
    mobilenumber=models.CharField(max_length=10,default="null")
    address = models.CharField(max_length=20, default="null")

