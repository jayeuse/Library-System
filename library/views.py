from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.

def home_page(request):
    return render(request, 'lib/home_page.html')

def student_list(request):

    query = request.GET.get("q")

    if query:
        students = Students.objects.filter(student_id__icontains=query)
    else:
        students = Students.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/student_rows.html', {'students': students})
    
    return render(request, "lib/students.html", {"students": students, "query": query})

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

    query = request.GET.get('q')

    if query:
        books = Books.objects.filter(title__icontains=query)
    else:
        books = Books.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/book_rows.html', {'books': books})
    

    return render(request, 'lib/books.html', {'books': books, 'query': query})

def insert_books(request):
    form = BookForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'lib/insert_books.html', {'form': form})
