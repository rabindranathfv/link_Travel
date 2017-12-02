# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf import settings

#Mail library
from django.core.mail import send_mail

#models UserMail
from .models import UserMail
from .forms import UserMailForm
# Create your views here.
def index(request):
	contact_f = UserMailForm(request.POST)
	if request.method == 'POST' and contact_f.is_valid():

		contact_f.save()

		contact_f.save()

		context = {}
		context['Name'] = contact_f.cleaned_data['Name']
		context['People'] = contact_f.cleaned_data['People']
		context['Email'] = contact_f.cleaned_data['Email']
		context['Topic'] = contact_f.cleaned_data['Topic']
		context['Phone'] = contact_f.cleaned_data['Phone']
		context['Message'] = contact_f.cleaned_data['Message']

		#Envio de mail para el usuario
		msg_plain = 'Hemos recibido su informacion satisfactoriamente. Proximamente nos estaremos contactando'
		msg_html = '<h1>Hemos recibido su informacion satisfactoriamente. Proximamente nos estaremos contactando<h1/>'
		
		send_mail(
				'Solicitud de contacto - Link Travel!', 			#titulo
				msg_plain,											#mensaje txt
				config('HOST_USER'),								#email de envio
				[contact_f.cleaned_data['Email']],					#destinatario
				fail_silently=False,
				html_message=msg_html,								#mensaje en html
				)

		send_mail(
				'Solicitud de contacto - Link Travel!', 			#titulo
				msg_plain,											#mensaje txt
				config('HOST_USER'),								#email de envio
				['rabindranathucv@gmail.com'],						#destinatario de control
				html_message=msg_html,								#mensaje en html
				)
		"""
		Aqui deberiamos enviar 2 correos, uno al que realizo el contacto
		y otro a nuestro propio correo de contacto de la empresa.

		"""
		return redirect('/#contact')

	return render(request, 'base.html')
