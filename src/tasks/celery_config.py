import os
import shutil
from celery import Celery
from configuration import config
from celery.schedules import crontab
from datetime import timedelta

celery_app = Celery("tasks", 
                    broker=f"redis://{config['celery_info']['host']}:{config['celery_info']['port']}",
                    backend=f"redis://{config['celery_info']['host']}:{config['celery_info']['port']}",
                    include= ['src.tasks.task'])




celery_app.conf.beat_schedule = {
    'clean-temp-folder-every-minute': {
        'task': 'src.tasks.task.clear_temp_folder',
        'schedule': crontab(minute=0),
    },
}