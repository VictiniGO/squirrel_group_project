from django.core.management.base import BaseCommand, CommandError
from squirrelapp.models import SquirrelDetail
import csv

class Command(BaseCommand):

    help = 'Import squirrel file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data', help="file containing squirrel details")
    
    def handle(self, *args, **options):
        file_=options['squirrel_data']
        
        with open(file_) as fp:
            reader=csv.DictReader(fp)
            for line in reader:
                obj = SquirrelDetail()
                obj.X = line['X']
                obj.save()
        
        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
