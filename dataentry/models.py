from django.db import models

class Student(models.Model):
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name



