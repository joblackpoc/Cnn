from django.db import models

# Create your models here.
class MultiStepFormModel(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    gplus=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects=models.Manager()