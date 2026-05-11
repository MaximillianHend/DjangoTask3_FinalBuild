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
