from django.shortcuts import render
from .models import StudentRegistration
from .form import StudentRegistrationForm
# Create your views here.

def  index(request):
    print(request.POST)
    if request.POST.get('email',None)!=None:
        student=StudentRegistration()
        student.first_name=request.POST.get('first_name')
        student.last_name=request.POST.get('last_name')
        student.password=request.POST.get('password')
        student.email=request.POST.get('email')
        student.gender=request.POST.get('gender')
        student.school=request.POST.get('school')
        student.save()
    
        

    return render(request,'index.html',{'form':StudentRegistrationForm})
