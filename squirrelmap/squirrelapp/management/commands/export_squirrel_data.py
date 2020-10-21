from django.core.management.base import BaseCommand, CommandError
from squirrelapp.models import SquirrelDetails
import csv

class Command(BaseCommand):
    help = 'Export squirrel file'
    def add_arguments(self, parser):
        parser.add_argument('squirrel_file_path', help="file path to be exported")
    def handle(self, *args, **options):
        path_=options['squirrel_file_path']
        with open(path_, 'w') as f:
            fieldnames = ['Latitude', 'Longitude', 'Unique_Squirrel_ID', 'Hectare', 'Shift', 'Date', 'Hectare_Squirrel_Number', 'Age', 'Primary_Fur_Color', 'Highlight_Fur_Color', 'Combination_of_Primary_and_Highlight_Color', 'Color_notes', 'Location', 'Above_Ground_Sighter_Measurement', 'Specific_Location', 'Running', 'Chasing', 'Climbing','Eating', 'Foraging', 'Other_Activities', 'Kuks', 'Quaas', 'Moans', 'Tail_flags', 'Tail_twitches', 'Approaches','Indifferent', 'Runs_from', 'Other_Interactions', 'Lat_Long']
            writer = csv.writer(f)
            writer.writerow(fieldnames)
            for obj in SquirrelDetails.objects.all():
                row = [getattr(obj, field) for field in fieldnames]
                writer.writerow(row)
            f.close()
        msg=f'Data written to {path_}'
        self.stdout.write(self.style.SUCCESS(msg))
