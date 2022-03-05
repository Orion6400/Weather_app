from django.shortcuts import render,HttpResponse
import urllib.request
import json
from .models import weather_data

def homepage(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=7bc29e275d67c72561195573b30ad78c').read()
        dict_data = json.loads(source)

        weather_data.objects.create(country_name=(str(city)).capitalize() ,country_code=str(dict_data["sys"]["country"]),
                                    coordinates=str(dict_data["coord"]["lon"])+"|"+str(dict_data["coord"]["lat"]),temp=str(dict_data["main"]["temp"]),
                                    real_temp_feel=str(dict_data["main"]["feels_like"]),pressure=str(dict_data["main"]["pressure"]),humidity=str(dict_data["main"]["humidity"]),
                                    wind_speed=str(dict_data["wind"]["speed"]),description=(str(dict_data["weather"][0]["description"])).capitalize())

        data = {
            "country_name": str(city),"country_code": str(dict_data["sys"]["country"]),"coordinates": str(dict_data["coord"]["lon"])+"|"+str(dict_data["coord"]["lat"]),
            "temp": str(dict_data["main"]["temp"]),"real_temp_feel": str(dict_data["main"]["feels_like"]),"pressure": str(dict_data["main"]["pressure"]),
            "humidity": str(dict_data["main"]["humidity"]),"wind_speed":str(dict_data["wind"]["speed"]),"description":str(dict_data["weather"][0]["description"])
        }
    else:
        data = {}

    return render(request,"main/index.html",{"data":data})

def recordpage(request):
    recorded_data = weather_data.objects.filter().values()
    return render(request,"main/record.html",{"record":recorded_data})

def deleterecord(request):
    if request.method == 'POST':
        id = request.POST['id']
    recorded_data = weather_data.objects.filter(id=id).delete()
    return render(request,"main/record.html",{"record":recorded_data})