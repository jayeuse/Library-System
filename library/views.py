from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home_page(request):
    return render(request, 'lib/home_page.html')

def student_list(request):
    students = Students.objects.all()
    return render(request, 'lib/students.html', {'students': students})

def insert_student(request):
    form = StudentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'lib/insert_student.html', {'form': form})

def book_list(request):
    books = Books.objects.all()
    return render(request, 'lib/books.html', {'books': books})

def insert_books(request):
    form = BookForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'lib/insert_books.html', {'form': form})
