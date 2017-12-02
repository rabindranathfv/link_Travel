# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class UserMail(models.Model):
    
    contact_id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50)
    People = models.IntegerField(default=1)
    Email = models.EmailField()
    Topic = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    Message = models.TextField(max_length = 250, blank = True)
    

    def __str__(self):
        return self.contact_id

    def __str__(self):
        return self.Name
