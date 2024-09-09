from django.core.management.base import BaseCommand, CommandParser
from dataentry.models import Student
import csv

class Command(BaseCommand):
    help = 'Import data from CSV File'

    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help='specifies file path')

    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        with open(f"{file_path}/student_data.csv",'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if Student.objects.filter(rollno=row['roll_no']).exists():
                    print(f"student with rollno {row['roll_no']} already present")
                    continue
                student = Student.objects.create(rollno=row['roll_no'],name=row['name'],age=row['age'])
        self.stdout.write(self.style.SUCCESS('Data imported from csv successfully'))