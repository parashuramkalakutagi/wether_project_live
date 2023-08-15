import pandas as pd
from django.http import HttpResponse

from rest_framework import filters
from rest_framework import viewsets
from rest_framework.response import Response

from .models import WeatherData
from .serializers import WeatherSerializers
from .weather_data import weather_data


class FetchWeatherData(viewsets.ViewSet):

    @staticmethod
    def create(request):
        data = request.data
        data = weather_data(data['lat'], data['lon'])
        return Response(data)


class Weather(viewsets.ModelViewSet):
    serializer_class = WeatherSerializers
    queryset = WeatherData.objects.all().order_by('?')
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['temp']
    ordering_fields = ['dt', 'sunrise', 'sunset']


class WeatherCSV(viewsets.ViewSet):

    @staticmethod
    def create(request):
        data = request.data
        dt = WeatherData.objects.filter(**data).values()
        df = pd.DataFrame(dt)

        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="weather_data.csv"'},
        )

        df.to_csv(response, index=False)

        return response
