
from django.shortcuts import get_object_or_404, render,redirect
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})

def home(request):
    return render(request, 'index.html')

def add_student(request):
        if request.method=="POST":
            Name = request.POST['name']
            Roll = request.POST['roll']
            Dept = request.POST['dept']
            Student.objects.create(name=Name,roll=Roll,department=Dept)
            return redirect("student_list")
        
        return render(request,"add_student.html")

def edit_student(request, roll):
    student = get_object_or_404(Student, roll=roll)

    if request.method=="POST":
        student.name = request.POST['name']
        student.department = request.POST['dept']
        student.save()
        return redirect("student_list")
    return render(request, "edit_student.html")

def delete_student(request, roll):
     student = get_object_or_404(Student, roll=roll)

     student.delete()
     return redirect("student_list")