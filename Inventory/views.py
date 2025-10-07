from django.shortcuts import render,redirect
from .models import *
from .forms import *
def Student_add(request):
    context ={
        'studentform':StudentForm()
    }
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
    return render(request,'student_add.html',context)
def student_list(request):
    context={
        "allstudents":Student.objects.all()
    }
    return render(request,'student_list.html',context)
def delete(request,id):
    select_student = Student.objects.get(id=id)
    select_student.delete()
    return redirect('/inventory/student/list/')

def update(request,id):
    select_student=Student.objects.get(id=id)
    context={
        "studentform":StudentForm(instance=select_student)
    }
    if request.method == "POST":
        studentform=StudentForm(request.POST, instance=select_student)
        if studentform.is_valid():
            studentform.save()
            return redirect('/inventory/student/list/')
    return render(request,'student_add.html',context)