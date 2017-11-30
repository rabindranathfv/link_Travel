# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.conf import settings

#Mail library
from django.core.mail import send_mail

# Create your views here.
def index(request):
	contact_f = core_forms.ContactForm(request.POST or None)
	if request.method == 'POST' and contact_f.is_valid():

		contact_f.save()

		contact_f.save()

		context = {}
		context['Name'] = contact_f.cleaned_data['requester_name']
		context['People'] = contact_f.cleaned_data['requester_mail']
		context['Email'] = contact_f.cleaned_data['']
		context['Topic'] = contact_f.cleaned_data['']
		context['Message'] = contact_f.cleaned_data['telephone_number']

		context['email_for'] = "user"

		#Envio de mail para el usuario
		msg_plain = render_to_string('core_app/mail/user_contact_email.txt', context)
		msg_html = render_to_string('core_app/mail/user_contact_email.html', context)

		send_mail(
				'Solicitud de contacto - Link Travel!', 			#titulo
				msg_plain,											#mensaje txt
				config('HOST_USER'),								#email de envio
				[contact_f.cleaned_data['requester_mail']],			#destinatario
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
