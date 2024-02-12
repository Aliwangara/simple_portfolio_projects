from email import message

from django.shortcuts import render
from .models import Contacts
from django.contrib import messages
from django.core.mail import send_mail
from django.core import  mail
from django.core.mail.message import EmailMessage
from  django.conf import settings
# Create your views here.
class Home:
    pass


def home(request):
    return render(request, 'Home.html')


def portfolio(request):
    return render(request, 'Portfolio.html')


def contact(request,):
    if request.method=="POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fsubject = request.POST.get('subject')
        fmessage = request.POST.get('message')

        query = Contacts(name=fname, email=femail, subject=fsubject, message=fmessage)
        query.save()
        #Email sending start
        from_email = settings.EMAIL_HOST_USER
        connection = mail.get_connection()
        connection.open()
        email_message = mail.EmailMessage(f'email is from {fname}', f'user email : {femail}\nuserPhoneNumber : {fsubject}\n\n\n query : {fmessage}'
                                          ,from_email, ['aliwangara63@gmail.com', 'wangaraali56@gmail.com'], connection=connection)

        email_client= mail.EmailMessage('Aliwangara response','Thanks for reaching me\n\n+254700331844\naliwangara63@gmail.com'
                                          ,from_email, [femail], connection=connection)


        connection.send_messages([email_message])
        connection.close()

        messages.success(request, "Thanks for contacting. I will get back to you soon!")
    return render(request, 'Contact.html')