from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['student_id', 'first_name', 'last_name', 'course', 'year_level', 'section']


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'author', 'isbn', 'published_date', 'available_copies']

class BorrowRecordForm(forms.ModelForm):
    class Meta:
        model = BorrowRecords
        fields = ['student', 'book', 'return_date']
