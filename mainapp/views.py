from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import ReservationTable, weeklyFeaturedFood, NewsLetter
from django.template.loader import  get_template
from django.core.mail import send_mail, EmailMultiAlternatives
from blogs.models import BlogsDatabase
from Restaurants import settings

def home(request):

        Blogs = BlogsDatabase.objects.all()
        blogs = BlogsDatabase.objects.all()[len(Blogs)-4:len(Blogs):-1]

        featuredFood = weeklyFeaturedFood.objects.all()
        context = {'blogs':blogs, 'weeklyfood':featuredFood}

        return render(request, 'mainapp_templates/index.html', context)

@login_required
def reservation(request):

        # If Request is POST Than it will Execute
        if request.method == 'POST':
                name = request.POST['name']
                phoneNumber = request.POST['phone']
                day = request.POST['day']
                time = request.POST['hour']
                num_persons = request.POST['persons']

                # Adding Form Data to aur Reservation Database
                reserve = ReservationTable()
                reserve.name = name
                reserve.phoneNumber = phoneNumber
                reserve.day = day
                reserve.time = time
                reserve.no_persons = num_persons

                # Commiting Our Changes
                reserve.save()

                # Sending Email After Reservation
                data = {'name':name,'phone':phoneNumber,'time':time,'day':day,'no_person':num_persons}
                mailMessage = 'Hello'
                message = EmailMultiAlternatives(subject=f'{name} Your Reservation has been Done!', body=mailMessage, from_email=settings.EMAIL_HOST_USER, to=[request.user.email])
                html_template = get_template('mainapp_templates/emailMessage.html').render(data)
                message.attach_alternative(html_template, "text/html")
                message.send()

                return redirect('HomePage')

@login_required
def newsLetter(request):

        if request.method == 'POST':
                email = request.POST['email']

                newsletter = NewsLetter()
                newsletter.email = email
                newsletter.save()

        data = {'email':request.user.email}
        mailMessage = "Dingo Restaurants"
        mail = EmailMultiAlternatives(subject=f'{request.user.email} Your Newsletter Update!', body=mailMessage, from_email=settings.EMAIL_HOST_USER, to=[request.user.email])
        html_template = get_template('mainapp_templates/newsletter.html').render(data)
        mail.attach_alternative(html_template, "text/html")
        mail.send()

        return redirect('HomePage')

def about(request):
    return render(request, 'mainapp_templates/About_us.html')


def menu(request):
    return render(request, 'mainapp_templates/menu.html')


def blog(request):
    return render(request, 'mainapp_templates/blog.html')

def contact(request):
    return render(request, 'mainapp_templates/contact.html')




