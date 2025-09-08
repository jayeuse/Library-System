from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/insert/', views.insert_student, name='insert_student'),
    path('books/', views.book_list, name='book_list'),
    path('books/insert/', views.insert_books, name='insert_books'),
]