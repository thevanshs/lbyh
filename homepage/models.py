from django.db import models

# Create your models here.

class Tutors(models.Model):
    name = models.CharField(max_length=70)
    qualification = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    linkdin = models.CharField(max_length=500 , null=True , blank=True)
    Xaccount = models.CharField(max_length=500 , null=True , blank=True)