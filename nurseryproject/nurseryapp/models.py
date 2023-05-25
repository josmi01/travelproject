from django.db import models
from django.shortcuts import render

# Create your models here.
class place(models.Model):
     name=models.CharField(max_length=250)
     img=models.ImageField(upload_to='pics')
     desc=models.TextField()
     def __str__(self):
         return self.name
class team(models.Model):
    image=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    def __str__(self):
        return self.name

