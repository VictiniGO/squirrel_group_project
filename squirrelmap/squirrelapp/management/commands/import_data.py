from django.core.management.base import BaseCommand, CommandError
from squirrelapp.models import SquirrelDetail

class Command(BaseCommand):
    help = 'Import squirrel file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data', help="file containing squirrel details")

    def handle(self, parser):
        file_=options['squirrel_data']

        with open(file_) as fp:
            reader=csv.DictReader(fp)

            for line in reader:
                obj = SquirrelDetail()


        msg=f'You are importing from {file_}'
