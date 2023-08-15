import random

from celery import shared_task
from datetime import timedelta
# from datetime import timezone
from django.utils import timezone
from .weather_data import weather_data
from random import randint




@shared_task(bind= True)
def wether_api_call_every_5minitus(self):
    weather_data(lat=12,lon=14)
    return " wether api called successfully...."