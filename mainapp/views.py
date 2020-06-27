from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ReservationTable
from django.template.loader import render_to_string , get_template
from django.core.mail import send_mail, EmailMultiAlternatives
from Restaurants import settings
import os

def home(request):

        return render(request, 'mainapp_templates/index.html')

@login_required
def reservation(request):
        if request.method == 'POST':
                name = request.POST['name']
                phoneNumber = request.POST['phone']
                day = request.POST['day']
                time = request.POST['hour']
                num_persons = request.POST['persons']

                reserve = ReservationTable()
                reserve.name = name
                reserve.phoneNumber = phoneNumber
                reserve.day = day
                reserve.time = time
                reserve.no_persons = num_persons

                reserve.save()

                data = {'name':name,'phone':phoneNumber,'time':time,'day':day,'no_person':num_persons}
                mailMessage = 'Hello'

                message = EmailMultiAlternatives(subject=f'{name} Your Reservation has been Done!', body=mailMessage, from_email=settings.EMAIL_HOST_USER, to=[request.user.email])
                html_template = get_template('mainapp_templates/emailMessage.html').render(data)
                message.attach_alternative(html_template, "text/html")
                message.send()

                return redirect('HomePage')

def about(request):
    return render(request, 'mainapp_templates/About_us.html')


def menu(request):
    return render(request, 'mainapp_templates/menu.html')


def blog(request):
    return render(request, 'mainapp_templates/blog.html')

def contact(request):
    return render(request, 'mainapp_templates/contact.html')




