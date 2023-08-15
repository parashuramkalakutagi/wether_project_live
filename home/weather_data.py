import requests
import time
import datetime
from .models import WeatherData
from pytz import timezone


def date(dtt):
    tm = time.localtime(dtt)
    d = datetime.datetime(tm.tm_year, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)
    am = d.astimezone(timezone('America/Chicago'))
    return am


def weather_data(lat, lon):
    api_key = "28d043c13638e96bc98e3361269f974f"
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}"

    result = requests.get(url)
    rs = result.json()

    print(rs)


    try:
        sea_level = rs['main']['sea_level']
    except:
        sea_level = None

    try:
        grnd_level = rs['main']['grnd_level']
    except:
        grnd_level = None

    try:
        wind_gust = rs['wind']['gust']
    except:
        wind_gust = None

    try:
        sys_type = rs['sys']['type']
        sys_id = rs['sys']['id']
        country = rs['sys']['country']
    except:
        sys_type = None
        sys_id = None
        country = None

    print(rs)

    data = WeatherData.objects.create(
        lon=rs['coord']['lon'],
        lat=rs['coord']['lat'],
        weather_id=rs['weather'][0]['id'],
        weather_main=rs['weather'][0]['main'],
        weather_description=rs['weather'][0]['description'],
        weather_icon=rs['weather'][0]['icon'],
        base=rs['base'],

        temp=rs['main']['temp'],
        feels_like=rs['main']['feels_like'],
        temp_min=rs['main']['temp_min'],
        temp_max=rs['main']['temp_max'],
        pressure=rs['main']['pressure'],
        humidity=rs['main']['humidity'],
        sea_level=sea_level,
        grnd_level=grnd_level,

        visibility=rs['visibility'],

        wind_speed=rs['wind']['speed'],
        wind_deg=rs['wind']['deg'],
        wind_gust=wind_gust,

        clouds_all=rs['clouds']['all'],

        dt=date(rs['dt']),
        sys_type=sys_type,
        sys_id=sys_id,
        country=country,
        sunrise=date(rs['sys']['sunrise']),
        sunset=date(rs['sys']['sunset']),

        timezone=rs['timezone'],
        key_first=rs['id'],
        name=rs['name']
    )

    return None


#weather_data(33.441792, -94.037689)
