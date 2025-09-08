from django.db import models
import uuid

class Students(models.Model):

    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False)
    
    student_id = models.CharField(max_length = 20, unique = True) # Assignable ID
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    course = models.CharField(max_length = 100)
    year_level = models.CharField(max_length = 10)
    section = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.student_id})"
    
class Books(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False)
    
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.IntegerField()

    def __str__(self):
        return f"{self.title} by {self.author}"
    

class BorrowRecords(models.Model):
    id = models.UUIDField(primary_key = True,
                          default = uuid.uuid4,
                          editable = False)
    
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} borrowed {self.book} on {self.borrow_date}"