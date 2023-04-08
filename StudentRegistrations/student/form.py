from django import forms
from .models import StudentRegistration

# Create your models here.
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model=StudentRegistration
        fields= '__all__'

