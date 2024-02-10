from email import message

from django.shortcuts import render
from .models import Contacts
from django.contrib import messages

# Create your views here.
class Home:
    pass


def home(request):
    return render(request, 'Home.html')


def portfolio(request):
    return render(request, 'Portfolio.html')


def contact(request):
    if request.method=="POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fsubject = request.POST.get('subject')
        fmessage = request.POST.get('message')
        query = Contacts(name=fname, email=femail, subject=fsubject, message=fmessage)
        query.save()
        messages.success(request, "Thanks for contacting. I will get back to you soon!")
    return render(request, 'Contact.html')