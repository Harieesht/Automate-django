# i want to add some data to the database using the custom command

from django.core.management.base import BaseCommand
from dataentry.models import *

class Command(BaseCommand):

    help='It will insert data to the database'

    def handle(self,*args,**kwargs):


        dataset=[
            {'rollno':'1002','name':'Harieesh','age':20},
            {'rollno':'1003','name':'Harieesh1','age':22},
            {'rollno':'1004','name':'Harieesh2','age':23},
        ]
        
        for data in dataset:
            rollno = data['rollno']
            existingrecord = Student.objects.filter(rollno=rollno).exists()
            if not existingrecord:    
                Student.objects.create(rollno=data['rollno'],name=data['name'],age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f"Student with rollno-{rollno} already exists"))
            
        self.stdout.write(self.style.SUCCESS("Data inserted successfully"))
