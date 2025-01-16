from django.shortcuts import render
from .models import News, Page, Teacher, Subject
from django.utils.translation import get_language
from django.utils import timezone
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect
from django.utils.translation import activate

# Create your views here.
def home_view(request):
    lang = get_language()
    page_item = Page.objects.filter(purpose="home").first()

    context = {'page_item': page_item,  'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'home.html', context)

def teachers_view(request):
    lang = get_language()
    teachers = Teacher.objects.all()

    context = {'teachers': teachers, 'lang': lang, }
    # returns render(request, template of certain product or element, context dictionary)
    return render(request, 'teachers.html', context)


def set_language(request):
    if request.method == "POST":
        language = request.POST.get('language')
        activate(language)
        response = HttpResponseRedirect(request.POST.get('next', '/'))
        response.set_cookie('django_language', language)
        return response
