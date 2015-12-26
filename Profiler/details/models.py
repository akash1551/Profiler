
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from time import time

def get_upload_file_name(instance, filename):
    return "images/%s_%s" %(str(time()).replace('.','_'),filename.replace(' ', '_'))


class Employee(models.Model):
    name=models.CharField(max_length=100)
    address=models.ForeignKey('Address')
    contact_no = models.IntegerField()
    thumbnail=models.FileField(upload_to=get_upload_file_name,blank=True,null=True)
    skills=models.ManyToManyField('Skills')

class Address(models.Model):
	address_line_1 = models.CharField(max_length=100)
	address_line_2 = models.CharField(max_length=100)
	city = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	pin_code = models.IntegerField()

class Skills(models.Model):
	skillset=models.CharField(max_length=100,blank=True,null=True)
	#skillset2=models.CharField(max_length=100,blank=True,null=True)

def __str__(self):
	return ' '.join([self.first_name,self.last_name,])