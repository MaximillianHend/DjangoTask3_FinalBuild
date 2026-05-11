"""
DjangoTask3_FinalBuild URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import path
from django.urls import include, re_path
<<<<<<< HEAD
#from django.views.generic.base import TemplateView #--------------------------------------------
=======

import MyApp.views


urlpatterns = [    
    path('admin/', admin.site.urls),
    path("", MyApp.views.index, name="index"),
    #path("about-us", MyApp.views.about_us, name="about_us"),
    #path("courses", MyApp.views.courses, name="courses"),
    #path("courses/json", MyApp.views.courses_json, name="courses_json"),
    #path("course/<str:course_name>", MyApp.views.course, name="course"),
    #path("new-course", MyApp.views.new_course, name="new_course"),
    #re_path(r'^$', MyApp.views.index, name='index'),
    re_path(r'^home$', MyApp.views.index, name='home'),
    #re_path(r'input', MyApp.views.input_view, name='input'),
]
