import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crypto_tracker.settings')

app = Celery('crypto_tracker')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    # 'test-celery-periodic': {
    #     'task': 'positions.tasks.create_test_object',
    #     'schedule': crontab(minute='*/1'),
    #     'kwargs': ({'name':'new2020'})
    # },
    # 'refresh-data': {
    #     'task': 'positions.tasks.refresh',
    #     'schedule': 60.0
    # }
    'fresh-data': {
        'task': 'positions.tasks.fresh_data',
        'schedule': 60.0
    }
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')