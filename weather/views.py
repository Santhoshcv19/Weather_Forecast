from django.shortcuts import render
from .forms import CityForm
from .models import Weather
import requests
from django.template import RequestContext

def index(request):
    form = CityForm()
    weather_data =  None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather_data(city)
            save_weather_data(weather_data)
    
    return render(request, 'weather/index.html', {'form':form, 'weather_data': weather_data})

def get_weather_data(city):
    api_key = 'a6ab6764f7c94a3795851017232112'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no'
    response = requests.get(url)
    data = response.json()
    return data

def save_weather_data(weather_data):
    Weather.objects.create(
        city = weather_data['location']['name'],
        temperature = weather_data['current']['temp_c'],
        humidity = weather_data['current']['humidity'],
        wind_speed = weather_data['current']['wind_kph']
    )