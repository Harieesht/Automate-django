from django.core.management.base import BaseCommand, CommandParser,CommandError
from django.apps import apps
import csv
from dataentry.models import *


class Command(BaseCommand):

    help = 'Import data from CSV File' #proposed commed - python manage.py file_path model_name

    def add_arguments(self,parser):
        parser.add_argument('file_path',type=str,help='specifies file path')
        parser.add_argument('model_name',type=str,help='Its the model name')

    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()

        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name) 
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f"Model {model_name} no found in any app")
        
        with open(file_path,'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)
        self.stdout.write(self.style.SUCCESS(f'Data imported from the model {model_name} successfully'))