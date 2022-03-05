from django.db import models
from datetime import date
# Create your models here.
class weather_data(models.Model):
    country_name = models.CharField(max_length=255,null=False)
    country_code= models.CharField(max_length=255,null=False)
    coordinates= models.CharField(max_length=255,null=False)
    temp= models.CharField(max_length=255,null=False)
    real_temp_feel= models.CharField(max_length=255,null=False)
    pressure= models.CharField(max_length=255,null=False)
    humidity= models.CharField(max_length=255,null=False)
    wind_speed= models.CharField(max_length=255,null=False)
    description= models.CharField(max_length=255,null=False)
    record_entry_date = models.DateTimeField(default=date.today)