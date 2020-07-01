from django.shortcuts import render, redirect
from .models import ContactsModel
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from Restaurants import settings

@login_required
def contactInfo(request):

        if request.method == 'POST':
                name = request.POST['name']
                phone = request.POST['phone']
                message = request.POST['message']

                contact = ContactsModel(name=name, email=request.user.email, phone=phone, message=message)
                contact.save()

                data = {'name':name, 'email':request.user.email,'phone':phone}
                mailMessage = 'Dingo Restaurants'
                mail = EmailMultiAlternatives(subject = f"{request.user.email}Your Contact Form Has been Sent Successfully!",body=mailMessage, from_email=settings.EMAIL_HOST_USER, to=[request.user.email])
                html_template = get_template('contacts/contactEmail.html').render(data)
                mail.attach_alternative(html_template, 'text/html')
                mail.send()

                return redirect('HomePage')

        return render(request, 'contacts/contact.html')