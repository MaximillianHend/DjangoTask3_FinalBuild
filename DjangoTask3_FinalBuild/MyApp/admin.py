from django.contrib import admin
from .models import teacher
from .models import school
from .models import course
from .models import subjects
# Register your models here.
admin.site.register(teacher)
admin.site.register(school)
admin.site.register(course)
admin.site.register(subjects)
