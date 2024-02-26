from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from enroll.forms import StudentRegistreation
from enroll.models import User
# Create your views here.
def add_show(request):
     stud=User.objects.all()
     if request.method=="POST":
          fm=StudentRegistreation(request.POST)
          if fm.is_valid():
               nm=fm.cleaned_data['name']
               em=fm.cleaned_data['email']
               pw=fm.cleaned_data['password']
               reg=User(name=nm,email=em,password=pw)
               reg.save() 
               fm=StudentRegistreation()          
     else:
           fm=StudentRegistreation()  
     return render(request,'addandshow.html',{'form':fm,'stu':stud})

# this fun will delete
def delete_data(request,id):
     if request.method=="POST":
          pi=User.objects.get(pk=id)
          pi.delete()
          return HttpResponseRedirect('/')
     
def update_data(request,id):
     if request.method=="POST":
          pi=User.objects.get(pk=id)
          fm=StudentRegistreation(request.POST,instance=pi)
          if fm.is_valid():
               fm.save()
     else:
          pi=User.objects.get(pk=id)
          fm=StudentRegistreation(instance=pi)          
     return render(request,'updatestudent.html',{'form':fm})     
