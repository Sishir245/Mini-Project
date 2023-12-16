from django.db import models

# Create your models here.
class Register(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)


class Appointment(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    num = models.IntegerField()
    comment = models.TextField(null=True,blank=True)
    date = models.DateField()
    time = models.TimeField()

class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    number = models.IntegerField()
    email = models.CharField(max_length=255)
    comment = models.TextField(null=True,blank=True)
