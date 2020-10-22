from django.forms import ModelForm
from .models import SquirrelDetails
class SquirrelRequestForm(ModelForm):
    class Meta:
        model = SquirrelDetails
        fields = [
                'Latitude',
                'Longitude',
                'Unique_Squirrel_ID',
                'Shift',
                'Date',
                'Age',
        ] 
