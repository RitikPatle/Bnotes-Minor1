from django.db import models

# Create your models here.
class Notes(models.Model):
    name = models.CharField(max_length=60)
    icon = models.ImageField(upload_to='pics')
    ref = models.CharField(max_length=60)

class Sub(models.Model):
    sem = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    pdf = models.FileField()
    
class Papers(models.Model):
    name = models.CharField(max_length=60)
    icon = models.ImageField(upload_to='pics')
    ref = models.CharField(max_length=60)

class Pub(models.Model):
    sem = models.CharField(max_length=100)
    stream = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    pdf = models.FileField()
    
class Post(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=60)
    mobno = models.CharField(max_length=10)
    comments = models.CharField(max_length=600)