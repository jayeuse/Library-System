from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home_page(request):
    return render(request, 'library/home_page.html')

def student_list(request):
    students = Students.objects.all()
    return render(request, 'library/students.html', {'students': students})

def insert_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'library/insert_student.html', {'form': form})

def book_list(request):
    books = Books.objects.all()
    return render(request, 'library/books.html', {'books': books})
