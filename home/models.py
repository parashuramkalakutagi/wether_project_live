from django.db import models

# Create your models here.


class WeatherData(models.Model):
    lon = models.FloatField(default=None)
    lat = models.FloatField()
    weather_id = models.IntegerField()
    weather_main = models.CharField(max_length=100)
    weather_description = models.CharField(max_length=100)
    weather_icon = models.CharField(max_length=100)
    base = models.CharField(max_length=100)

    temp = models.FloatField()
    feels_like = models.FloatField()
    temp_min = models.FloatField()
    temp_max = models.FloatField()
    pressure = models.FloatField()
    humidity = models.FloatField()
    sea_level = models.FloatField(null=True)
    grnd_level = models.FloatField(null=True)

    visibility = models.FloatField()

    wind_speed = models.FloatField()
    wind_deg = models.FloatField()
    wind_gust = models.FloatField(null=True)

    clouds_all = models.FloatField()

    dt = models.DateTimeField()
    sys_type = models.IntegerField(null=True)
    sys_id = models.IntegerField(null=True)
    country = models.CharField(max_length=100, null=True)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()

    timezone = models.IntegerField(default=None)
    key_first= models.IntegerField(default=None)
    name = models.CharField(max_length=100, null=True)