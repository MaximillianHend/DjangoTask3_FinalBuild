from django import forms
from .models import teacher
#from .models import school
#from .models import course
#from .models import subjects

class CourseForm(forms.Form):
   name = forms.CharField(label="Name", max_length=128)
   enrolled_students = forms.IntegerField(label="Students")


#class InputForm(forms.ModelForm):
#    class Meta:
 #       model = school
  #      fields = ['School_Name', 'Location']


#class InputForm(forms.ModelForm):
 #   class Meta:
  #      model = course
   #     fields = ['Course', 'Scalinig', 'Teachers']

        
#class InputForm(forms.ModelForm):
 #   class Meta:
  #      model = subjects
   #     fields = ['Subjects']