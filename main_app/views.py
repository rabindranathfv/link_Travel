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
    
    if request.method == 'POST':
        contact_f = UserMailForm(request.POST)
        if contact_f.is_valid():

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
                    'Solicitud de contacto - Link Travel!',             #titulo
                    msg_plain,                                            #mensaje txt
                    config('HOST_USER'),                                #email de envio
                    [contact_f.cleaned_data['Email']],                    #destinatario
                    fail_silently=False,
                    html_message=msg_html,                                #mensaje en html
                    )

            send_mail(
                    'Solicitud de contacto - Link Travel!',             #titulo
                    msg_plain,                                            #mensaje txt
                    config('HOST_USER'),                                #email de envio
                    ['rabindranathucv@gmail.com'],                        #destinatario de control
                    fail_silently=False,
                    html_message=msg_html,                                #mensaje en html
                    )
            return redirect('/#contact')
    contact_f = UserMailForm()
    return render(request, 'base.html',{'form':contact_f})
