from django.shortcuts import render
import json
import datetime
import requests
# Create your views here.
def home(request):
    if 'city' in request.POST:
        city=request.POST['city'].lower()
    else:
        city='dhaka'
    appid='2945bcf642ab478cc11bb36c7ce16026'
    URL='http://api.openweathermap.org/data/2.5/weather'
    params={'q': city,'appid':appid,'units':'metric'}
    obj=requests.get(url=URL,params=params)
    r = obj.json()
    description = r['weather'][0]['description']
    icon = r['weather'][0]['icon']
    temp = r['main']['temp']
    day=datetime.date.today()
    context={
        'description':description,
        'icon':icon,
        'temp':temp,
        'day':day,
        'city':city,
    }
    return render(request,'helper/index.html',context)