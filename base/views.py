from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect
from .models import Certification, Project, Post, Skill
from django.core.mail import send_mail
from django.contrib import messages 

@csrf_protect
def home(request):
    projects = Project.objects.all()
    certifications = Certification.objects.all()
    skills = Skill.objects.all()
    posts = Post.objects.all().order_by('-created_at')
    context = {
        'projects': projects,
        'certifications': certifications,
        'posts': posts,
        'skills' :skills
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        if username == "" or email_address == "" or message == "":
            messages.warning(request, "There is one or more fields are empty!")
            return redirect('../#contact')
        else:
            data = {
                'username': username,
                'email_address': email_address,
                'message': message
            }
            email_message = ''' 
            New message: {}
            From {}
            '''.format(data['message'], data['email_address'])
            send_mail(data['username'], email_message, data['email_address'], ['sviatoslav.popina@gmail.com'])
            messages.success(request, "Your message has been sent successfully!")
            return redirect('../#contact')
    return render(request, 'base/main.html', context)

def about(request):
    return render(request, 'base/about.html')

def skills(request):
    skills = Skill.objects.all()
    return render(request, 'base/skills.html', {'skills': skills})

def projects(request):
    projects = Project.objects.all()
    context = {'projects': projects}
    return render(request, 'base/projects.html', context)

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'base/project_detail.html', {'project': project})

def certification_list(request):
    certifications = Certification.objects.all()
    return render(request, 'base/certification_list.html', {'certifications': certifications})

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'base/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'base/post_detail.html', {'post': post})

def contact(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email_address = request.POST.get('email_address')
        message = request.POST.get('message')

        if username == "" or email_address == "" or message == "":
            messages.warning(request, "There is one or more fields are empty!")
            return redirect('../#contact')
        else:
            data = {
                'username': username,
                'email_address': email_address,
                'message': message
            }
            email_message = ''' 
            New message: {}
            From {}
            '''.format(data['message'], data['email_address'])
            send_mail(data['username'], email_message, data['email_address'], ['sviatoslav.popina@gmail.com'])
            messages.success(request, "Your message has been sent successfully!")
            return redirect('../#contact')
    return render(request, 'base/contact.html')
