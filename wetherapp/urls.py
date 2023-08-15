
from django.contrib import admin
from django.urls import path,include
from home.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('FetchWeatherData',FetchWeatherData,basename='FetchWeatherData')
router.register('Weather',Weather,basename='Weather')
router.register('WeatherCSV',WeatherCSV,basename='WeatherCSV')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls))

]
