from django.shortcuts import render,HttpResponse,redirect
import urllib.request
import json
from .models import weather_data
from datetime import datetime

def homepage(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=7bc29e275d67c72561195573b30ad78c').read()
        dict_data = json.loads(source)
        cur_time = datetime.now().replace(tzinfo=None).strftime("%m/%d/%Y, %H:%M:%S")

        weather_data.objects.create(country_name=(str(city)).capitalize() ,country_code=str(dict_data["sys"]["country"]),
                                    coordinates=str(dict_data["coord"]["lon"])+"|"+str(dict_data["coord"]["lat"]),temp=str(dict_data["main"]["temp"]),
                                    real_temp_feel=str(dict_data["main"]["feels_like"]),pressure=str(dict_data["main"]["pressure"]),humidity=str(dict_data["main"]["humidity"]),
                                    wind_speed=str(dict_data["wind"]["speed"]),description=(str(dict_data["weather"][0]["description"])).capitalize(),record_entry_date=str(cur_time))

        data = {
            "country_name": str(city),"country_code": str(dict_data["sys"]["country"]),"coordinates": str(dict_data["coord"]["lon"])+"|"+str(dict_data["coord"]["lat"]),
            "temp": str(dict_data["main"]["temp"]),"real_temp_feel": str(dict_data["main"]["feels_like"]),"pressure": str(dict_data["main"]["pressure"]),
            "humidity": str(dict_data["main"]["humidity"]),"wind_speed":str(dict_data["wind"]["speed"]),"description":str(dict_data["weather"][0]["description"]),"Time":cur_time
        }
    else:
        data = {}

    return render(request,"main/index.html",{"data":data})

def recordpage(request):
    recorded_data = weather_data.objects.filter().values()
    if request.method == 'POST':
        id = request.POST.get('sno')
        try:
            print(id)
            weather_data.objects.filter(id=id).delete()
        except Exception as e:
            print(e)
        return redirect('http://127.0.0.1:8000/record/')
    return render(request,"main/record.html",{"record":recorded_data})

