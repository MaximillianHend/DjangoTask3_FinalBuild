from django import forms

from .models import teacher, school, course, subject

class InputForm(forms.ModelForm):
    class Meta:
        model = teacher
        fields = ['Name', 'Area']

class InputForm(forms.ModelForm):
    class Meta:
        model = school
        fields = ['School', 'Location']

class InputForm(forms.ModelForm):
    class Meta:
        model = course
        fields = ['Course', 'Scaling', 'Teachers']

class InputForm(forms.ModelForm):
    class Meta:
        model = subject
        fields = ['Subjects']
    

    SUBJECTS = (
        (1, "Maths"),
        (2, "English"),
        (3, "HASS"),
        (4, "Exercise Science"),
        (5, "IT"),
    )
    time = forms.ChoiceField(label="Subjects", choices=SUBJECTS)
    

    tertiary = forms.BooleanField(label="Tertiary", required=False)


'''


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

'''