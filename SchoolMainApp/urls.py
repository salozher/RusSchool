from django.contrib import admin
from django.urls import path

from SchoolMainApp.views import (home_view, teachers_view, )

urlpatterns = [

    path('', home_view, name='home'), path('team/', teachers_view, name='team'),

]
