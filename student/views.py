from django.shortcuts import render
from django.http import HttpResponse
from .models import StudentRegistration
from .form import StudentRegistrationForm,LoginForm
from django.shortcuts import get_object_or_404

# Create your views here.
def login(request):
    return render(request,'login.html',{'form':LoginForm})
def checkLogin(request):
    if request.POST.get('email',None)!=None:
        try:
            #print(request.POST.get('email',None))
            #print(request.POST.get('password'))
            studentdata=StudentRegistration.objects.get(email= request.POST.get('email'))
            if studentdata.password == request.POST.get('password'):
                return HttpResponse("Login Successfull !!")
        except:
            return HttpResponse("Login Unsuccessfull !!")

    return HttpResponse("Login Unsuccessfull !!")

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
