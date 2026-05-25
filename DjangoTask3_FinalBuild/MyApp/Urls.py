from django.urls import include, re_path
import MyApp.views

"""
Inclass_Django_1 URL Configuration

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

urlpatterns = [
    # this is how the 
    path('admin/', admin.site.urls),
    re_path(r'^$', MyApp.views.index, name='index'),
    re_path(r'^home$', MyApp.views.index, name='home'),
    re_path(r'teacherinput', MyApp.views.teacherinput_view, name='teacherinput'),
    re_path(r'schoolinput', MyApp.views.schoolinput_view, name='schoolinput'),
    re_path(r'courseinput', MyApp.views.courseinput_view, name='courseinput'),
    re_path(r'subjectinput', MyApp.views.subjectinput_view, name='subjectinput'),
]
