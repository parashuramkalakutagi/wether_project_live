from rest_framework import serializers

from .models import WeatherData


class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'