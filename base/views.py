# Create your views here.
from django.shortcuts import render, redirect
from .models import Project
from django.core.mail import send_mail
from django.contrib import messages


def home(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    if request.method == 'POST':

        username = request.POST.get('username')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        if username == "" or email_address == "" or message == "":
            messages.warning(request, "There is one or more fields are empty!")
            redirect('base/contact.html')
        else:

            data = {
                'username': username,
                'email_address': email_address,
                'message': message
            }
            message = ''' 
            New message: {}
            From {}
            '''.format(data['message'], data['email_address'])
            send_mail(data['username'], message, data['email_address'], ['sviatoslav.popina@gmail.com'])
    return render(request, 'base/main.html', context)


def about(request):
    return render(request, 'base/about.html')

def skills(request):
    return render(request, 'base/skills.html')

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)


def contact(request):
    return render(request, 'base/contact.html')