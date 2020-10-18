from django.core.management.base import BaseCommand, CommandError
from squirrelapp.models import SquirrelDetails
import csv
import json

class Command(BaseCommand):

    help = 'Import squirrel file'

    def add_arguments(self, parser):
        parser.add_argument('squirrel_data', help="file containing squirrel details")
    
    def handle(self, *args, **options):
        file_=options['squirrel_data']
        
        with open(file_) as fp:
            reader=csv.DictReader(fp)
            for line in reader:
                obj = SquirrelDetails()
                obj.Latitude = line['X']
                obj.Logitude = line['Y']
                obj.Unique_Squirrel_ID= line['Unique Squirrel ID']
                obj.Hectare=line['Hectare']
                obj.Shift=line['Shift']
                obj.Date=line['Date']
                obj.Hectare_Squirrel_Number=line['Hectare Squirrel Number']
                obj.Age=line['Age']
                obj.Primary_Fur_Color=line['Primary Fur Color']
                obj.Highlight_Fur_Color=line['Highlight Fur Color']
                obj.Combination_of_Primary_and_Highlight_Color=line['Combination of Primary and Highlight Color']
                obj.Color_notes=line['Color notes']
                obj.Location=line['Location']
                obj.Above_Ground_Sighter_Measurement=line['Above Ground Sighter Measurement']
                obj.Specific_Location=line['Specific Location']
                obj.Running= json.loads(line['Running'].lower())
                obj.Chasing=json.loads(line['Chasing'].lower())
                obj.Climbing=json.loads(line['Climbing'].lower())
                obj.Eating=json.loads(line['Eating'].lower())
                obj.Foraging=json.loads(line['Foraging'].lower())
                obj.Other_Activities=line['Other Activities']
                obj.Kuks=json.loads(line['Kuks'].lower())
                obj.Quaas=json.loads(line['Quaas'].lower())
                obj.Moans=json.loads(line['Moans'].lower())
                obj.Tail_flags=json.loads(line['Tail flags'].lower())
                obj.Tail_twitches=json.loads(line['Tail twitches'].lower())
                obj.Approaches=json.loads(line['Approaches'].lower())
                obj.Indifferent=json.loads(line['Indifferent'].lower())
                obj.Runs_from=json.loads(line['Runs from'].lower())
                obj.Other_Interactions=line['Other Interactions']
                obj.Lat_Long=line['Lat/Long']
                obj.save()
        
        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
