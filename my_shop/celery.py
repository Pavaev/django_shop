import os
from celery import Celery
from celery.schedules import crontab

from my_shop import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_shop.settings')

app = Celery('my_shop')
app.config_from_object(settings)

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'products.tasks.send_view_count_report',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}