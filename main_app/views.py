# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.conf import settings

#Mail library
from django.core.mail import send_mail

# Create your views here.
def index(request):
	return render(request, 'base.html')

def contactanos(request):
	return render(request,'base.html')