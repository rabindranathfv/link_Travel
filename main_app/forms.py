# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

# para Renderizar los froms con widgets
from django.utils.translation import ugettext_lazy as _

from .models import UserMail

# Create your models here
class UserMailForm(forms.ModelForm):
    
  #  Name = forms.CharField(max_length=50,required=True)
  #  People = forms.IntegerField(default=1)
  #  Email = forms.EmailField()
  #  Topic = forms.CharField(max_length=100)
  #  phone_number = forms.CharField(max_length=15)
  #  Message = forms.TextField(max_length = 250, blank = True)


    class Meta:
		model = UserMail

		fields = ['Name', 'People', 'Email', 'Topic', 'Phone','Message']

		labels = {	'Name':_('Nombre de contacto'),
                    'People':_('Cantidad de personas'),
					'Email':_('Correo Electrónico'),
					'Topic':_('Topico'),
					'Phone':_('Telefono'),
					'Message':_('Mensaje'),
				}
		
		widgets = {	'Name': forms.TextInput(attrs={'class':'w3-input w3-padding-16 w3-border' , 'placeholder':'Nombre/Name'}),
                    'People' : forms.TextInput(attrs={'class':'w3-input w3-padding-16 w3-border' , 'placeholder':'Cuantas personas/How many people?.'}),
					'Email': forms.EmailInput(attrs={'class':'w3-input w3-padding-16 w3-border' , 'placeholder':'Correo Electronico/Email'}),
					'Topic': forms.TextInput(attrs={'class':'w3-input w3-padding-16 w3-border','placeholder':'Topico/Topic.'}),
					'Phone': forms.TextInput(attrs={'class':'w3-input w3-padding-16 w3-border' , 'pattern':'\d{7,15}', 'placeholder':'Telefono/Phone Number'}),
					'Message': forms.Textarea(attrs={'class':'w3-input w3-padding-16 w3-border', 'placeholder':'Máximo 500 caracteres/ Maximun 500 Characters'}),
				}