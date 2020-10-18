from django.core.management.base import BaseCommand
class Command(BaseCommand):
    
    help = 'Import squirrel file'
    
    def add_arguments(self, parser):
        parser.add_argument('squirrel_data', help="file containing squirrel details")
    
    def handle(self,*args,**options):
        file_=options['squirrel_data']
        
        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
