from django.db import models

class SquirrelDetails(models.Model):
    Latitude = models.DecimalField(
            max_digits=11, 
            decimal_places=8,
    )

    Longitude = models.DecimalField(
            max_digits=11, 
            decimal_places=8,
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=14,
        primary_key=True,
    )

    Hectare = models.CharField(
        max_length=3,
        blank=True,
    )
    
    SHIFT_CHOICES = [
    ('AM','AM'),
    ('PM','PM'),
]

    Shift = models.CharField(
        max_length=2,
        choices=SHIFT_CHOICES,
    )

    Date = models.CharField(max_length=10)

    Hectare_Squirrel_Number = models.IntegerField(
        blank=True,
        null=True,
    )

    AGE_CHOICES = [
    ('Adult','Adult'),
    ('Juvenile','Juvenile'),
    ('',''),
]
    
    Age = models.CharField(
        max_length=10,
        choices=AGE_CHOICES,
    )

    PRIMARY_FUR_COLOR_CHOICES = [
    ('Gray','Gray'),
    ('Cinnamon','Cinnamon'),
    ('Black','Black'),
]
        
    Primary_Fur_Color = models.CharField(
        max_length=10,
        choices=PRIMARY_FUR_COLOR_CHOICES,
        blank=True,
    )


    Highlight_Fur_Color = models.CharField(
        max_length=50,
        blank=True,
    )
    

    Combination_of_Primary_and_Highlight_Color = models.CharField(
        max_length=50,
        blank=True,
    )

    Color_notes = models.CharField(
        max_length=50,
        blank=True,
    )

    LOCATION_CHOICES = [
    ('Ground Plane','Ground Plane'),
    ('Above Ground','Above Ground'),
]
    
    Location = models.CharField(
        max_length=20,
        choices=LOCATION_CHOICES,
        null=True,
        blank=True,
    )

    Above_Ground_Sighter_Measurement= models.CharField(
        max_length=10,
        blank=True,
    )

    Specific_Location = models.CharField(
        max_length=50,
        blank=True,
    )

    Running = models.BooleanField(
        blank=True,
        null=True,
    )

    Chasing = models.BooleanField(
        blank=True,
        null=True,
    )

    Climbing = models.BooleanField(
        blank=True,
        null=True,
    )
    
    Eating = models.BooleanField(
        blank=True,
        null=True,
    )   
    
    Foraging = models.BooleanField(
        blank=True,
        null=True,
    )
    
    Other_Activities = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    
    Kuks = models.BooleanField(
        null=True,
        blank=True,
    )  
    
    Quaas  = models.BooleanField(
        blank=True,
        null=True,
    )  
    
    Moans = models.BooleanField(
        blank=True,
        null=True,
    )      
    
    Tail_flags = models.BooleanField(
        blank=True,
        null=True,
    ) 
    
    Tail_twitches = models.BooleanField(
        blank=True,
        null=True,
    )       

    Approaches  = models.BooleanField(
        blank=True,
        null=True,
    )
    
    Indifferent = models.BooleanField(
        blank=True,
        null=True,
    )
    
    Runs_from  = models.BooleanField(
        blank=True,
        null=True,
    ) 
    
    Other_Interactions = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )  
    
    Lat_Long = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

