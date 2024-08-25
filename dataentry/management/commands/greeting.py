from django.core.management.base import BaseCommand

#proposed output
class Command(BaseCommand):

    help = 'It is a greeting command'

    def add_arguments(self,parser):
        parser.add_argument('name',type=str,help='Specifies username')

    def handle(self,*args,**kwargs):
        name=kwargs['name']
        self.stdout.write(self.style.SUCCESS(f"Hi {name} good morning"))
