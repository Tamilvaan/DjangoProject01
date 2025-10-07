from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100,unique=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    course = models.CharField(max_length=50)
    date_joined = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name+" "+self.last_name