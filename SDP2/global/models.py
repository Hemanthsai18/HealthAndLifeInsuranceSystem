from os import name
from django.db import models

# Create your models here.

class Health_Insurance(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    pdf = models.FileField(upload_to='pdfs', default='settings.MEDIA/pdfs/TERM INSURANCE.pdf')

class Life_Insurance(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    pdf = models.FileField(upload_to='pdfs', default='settings.MEDIA/pdfs/TERM INSURANCE.pdf')


class Details(models.Model):
    name = models.CharField(max_length=150)
    age = models.CharField(max_length=100,null=True)
    newid = models.IntegerField(null=True)
    amount = models.IntegerField()
    year = models.IntegerField()
    typo = models.IntegerField()
    total = models.IntegerField()
    month = models.IntegerField(null=True)
    start_date=models.CharField(max_length=100,null=True)

class User_Own(models.Model):
    user_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    # details = models.ManyToManyField(Details)
    email = models.EmailField()