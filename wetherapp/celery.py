from __future__ import absolute_import ,unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wetherapp.settings')
app = Celery('wetherapp')
app.conf.enable_utc = False
app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings,namespace='CELERY')

app.autodiscover_tasks()

#celery beat


# scheduled to delete object on particular time
app.conf.beat_schedule = {
    'wether_api_call_5_minitus':{
        'task':'home.tasks.wether_api_call_every_5minitus',
        'schedule':crontab(hour='*',minute='*/2'),
    }

}



@app.task(bind = True)
def debug_task(self):
    print(f'Request : {self.request!r}')
