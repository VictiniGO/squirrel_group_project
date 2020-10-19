from django.db import models

class SquirrelDetails(models.Model):
    Latitude = models.DecimalField(
            max_digits=15, 
            decimal_places=10,
            null=True)

    Longitude = models.DecimalField(
            max_digits=15,
            decimal_places=10,
            null=True)

    Unique_Squirrel_ID = models.CharField(
        max_length=20,
        primary_key=True,
    )

    Hectare = models.CharField(max_length=3)
    
    SHIFT_CHOICES = [
    ('AM','AM'),
    ('PM','PM'),
]

    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
    )

    Date = models.CharField(max_length=8)

    Hectare_Squirrel_Number = models.IntegerField

    AGE_CHOICES = [
    ('Adult','Adult'),
    ('Juvenile','Juvenile'),
]
    
    Age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
        null=True,
    )

    PRIMARY_FUR_COLOR_CHOICES = [
    ('Gray','Gray'),
    ('Cinnamon','Cinnamon'),
    ('Black','Black'),
]
        
    Primary_Fur_Color = models.CharField(
        max_length=10,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        null=True,
    )

        
    Highlight_Fur_Color = models.CharField(
        max_length=50
    )
    

    Combination_of_Primary_and_Highlight_Color = models.CharField(
        max_length=50
    )

    Color_notes = models.CharField(
        max_length=50
    )

    LOCATION_CHOICES = [
    ('Ground Plane','Ground Plane'),
    ('Above Ground','Above Ground'),
]
    
    Location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        null=True,
    )

    Above_Ground_Sighter_Measurement= models.CharField(
        max_length=10
    )

    Specific_Location = models.CharField(
        max_length=50
    )

    Running = models.BooleanField(
        null=False,
    )

    Chasing = models.BooleanField(
        null=False,
    )

    Climbing = models.BooleanField(
        null=False,
    )
    
    Eating = models.BooleanField(
        null=False,
    )   
    
    Foraging = models.BooleanField(
        null=False,
    )
    
    Other_Activities = models.CharField(
        max_length=50
    )
    
    Kuks = models.BooleanField(
        null=False,
    )  
    
    Quaas  = models.BooleanField(
        null=False,
    )  
    
    Moans = models.BooleanField(
        null=False,
    )      
    
    Tail_flags = models.BooleanField(
        null=False,
    ) 
    
    Tail_twitches = models.BooleanField(
        null=False,
    )       
    
    Approaches  = models.BooleanField(
        null=False,
    )
    
    Indifferent = models.BooleanField(
        null=False,
    )
    
    Runs_from  = models.BooleanField(
        null=False,
    ) 
    
    Other_Interactions = models.CharField(
        max_length=50
    )  
    
    Lat_Long = models.CharField(
        max_length=50
    )
