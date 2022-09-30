from django.db import models

# Create your models here.
class signup(models.Model):
    Name = models.CharField(max_length=20)
    Username = models.CharField(max_length=20)
    Password = models.CharField(max_length=20)
    Email = models.CharField(max_length=40)
    Status = models.BooleanField(default=False)
    File = models.FileField()

class ldetails(models.Model):
    Fname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    Email_ID = models.CharField(max_length=30)
    Phone = models.CharField(max_length=13)
    Status = models.BooleanField(default=False)


class addlease(models.Model):
    Wcountry = models.CharField(max_length=30)
    Dcountry = models.CharField(max_length=30)
    
    
class client(models.Model):
    Fromdate = models.DateField()
    Todate = models.DateField()
    Sizecontain = models.CharField(max_length=20)
    Ratecontain = models.CharField(max_length=20)
    Containername = models.CharField(max_length=20)
    Customersname = models.CharField(max_length=20)
    