from django.contrib import admin
from .models import weather_data
# Register your models here.

class Weather_dataAdmin(admin.ModelAdmin):
    list_display = ["country_name","country_code","coordinates","temp","real_temp_feel","pressure","humidity","wind_speed","description"]
admin.site.register(weather_data, Weather_dataAdmin)