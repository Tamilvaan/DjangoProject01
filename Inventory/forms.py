from django.forms import ModelForm
from .models import *

class StudentForm(ModelForm):


    class Meta:

        model = Student

        fields = ['first_name','last_name','email','enrollment_number','course']