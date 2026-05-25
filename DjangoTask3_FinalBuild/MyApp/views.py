from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import teacher, school, course, subject
from .forms import InputForm
import sqlite3
import django.db 
# Create your views here.

def index (request):    

    teach = teacher.objects.all()
    return render(request, "MyApp/index.html", {'content': teach})

def index (request):

    sch = school.objects.all()
    return render(request, "MyApp/index.html", {'content': sch})

def index (request):

    crs = course.objects.all()
    return render(request, "MyApp/index.html", {'content': crs})

def index (request):

    sub = subject.objects.all()
    return render(request, "MyApp/index.html", {'content': sub})
        

def teacherinput_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()

    return render(request, "MyApp/teacherinput.html", {"form": form})

def schoolinput_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()

    return render(request, "MyApp/schoolinput.html", {"form": form})

def courseinput_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
  
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()

    return render(request, "MyApp/courseinput.html", {"form": form})


def subjectinput_view(request):
    if request.method == "POST":
        form = InputForm(request.POST)
  
        if form.is_valid():
            form.save()
            return redirect("index")

    else:
        form = InputForm()
 
    return render(request, "MyApp/subjectinput.html", {"form": form})


'''
from django.shortcuts import render, redirect
from .models import teacher
from .models import school
from .forms import forms


def index(request):
    teach = teacher.objects.all()
    return render(request, "InclassDjango1/index.html", {'content': teach})

def index(request):
    sch = school.objects.all()
    return render(request, "InclassDjango1/index.html", {'content': sch})


def new_course(request: HttpRequest) -> HttpResponse:
    form = forms.CourseForm()
    ctx = {"form": form}
    return render(request, "myapp/input.html", ctx)


<<<<<<< HEAD
=======
        else: 
            form = InputForm()
  
    return render(request, "MyApp/index.html", {'form': form})

def index(request):
    return HttpResponse("Hello, Django!")
>>>>>>> 6dcec45553daad9f656ba31aa440dd45e8742106
'''