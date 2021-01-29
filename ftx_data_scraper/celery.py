import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ftx_data_scraper.settings')

app = Celery('ftx_data_scraper')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get-futures-markets': {
        'task': 'futures.tasks.get_futures_markets',
        'schedule': 60.0
    }
}

# app.conf.beat_schedule = {
#     'get-and-calculate-spreads': {
#         'task': 'futures.tasks.get_and_calculate_spreads',
#         'schedule': 1.0
#     }
# }

app.autodiscover_tasks()
