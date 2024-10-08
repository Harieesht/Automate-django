import csv 

from django.core.management.base import BaseCommand, CommandParser,CommandError
from dataentry.models import *
from django.apps import apps
import datetime

class Command(BaseCommand):

    help='command for exporting the data' #python manage.py exportdata model_name


    def add_arguments(self, parser):
        parser.add_argument('model_name',type=str ,help='selected model')

    def handle(self,*args,**kwargs):

        model_name = kwargs['model_name']

        model = None

        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label,model_name)
                break #stop execute once the model is found

            except LookupError:
                continue

        if not model:
            self.stderr.write(f"Model {model_name} could not be found")
            return 


        datas = model.objects.all()

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        file_path = f'exported_{model_name}_data_{timestamp}.csv'
        
        with open(file_path,'w',newline='') as file:
            writer = csv.writer(file)

            writer.writerow([field.name for field in model._meta.fields])

            for data in datas:
                writer.writerow([getattr(data,field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS("data exported successfully"))