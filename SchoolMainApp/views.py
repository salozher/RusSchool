from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.utils.translation import get_language
from django.core.mail import send_mail
from django.conf import settings
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

from SchoolMainApp.forms import Contact

from .models import Page, Teacher

# Create your views here.
def home_view(request):
    lang = get_language()
    page_item = Page.objects.filter(purpose="home").first()

    context = {'page_item': page_item, 'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'home.html', context)

def team_view(request):
    lang = get_language()
    teachers = Teacher.objects.all()

    context = {'teachers': teachers, 'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'team.html', context)

def about_view(request):
    lang = get_language()
    teachers = Teacher.objects.all()

    context = {'teachers': teachers, 'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'about.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = Contact(request.POST)
        if form.is_valid():
            try:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                kids_age = form.cleaned_data['kids_age']
                selected_subjects = form.cleaned_data['subjects']  # List of selected subjects

                # Send an email
                response = send_mail(subject=f"Contact Form Message from {name}", message=f"From: {email}\nName:{name}\nMessage: {message}\nChild's Age: {kids_age}\nSelected Subjects: {', '.join(selected_subjects)}", from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[settings.DEFAULT_FROM_EMAIL, email], fail_silently=False, )
                print(response)



            except Exception as e:
                logging.error(f"Email sending failed: {e}")
                return render(request, 'error.html', {'error': 'Failed to send the email.'})

        return render(request, 'success.html')

    else:
        form = Contact()

    return render(request, 'contact.html', {'form': form})

def news_view(request):
    lang = get_language()
    teachers = Teacher.objects.all()

    context = {'teachers': teachers, 'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'news.html', context)

def set_language(request):
    if request.method == "POST":
        language = request.POST.get('language')
        activate(language)
        response = HttpResponseRedirect(request.POST.get('next', '/'))
        response.set_cookie('django_language', language)
        return response

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Replace with your desired redirect
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
