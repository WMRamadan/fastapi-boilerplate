"""Celery worker."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import time
from functools import lru_cache
from celery import Celery
from . import config


@lru_cache()
def get_settings():
    """
    Config settings function.
    """
    return config.Settings()

conf_settings = get_settings()

celery = Celery(__name__)
celery.conf.broker_url = conf_settings.CELERY_CONF_BROKER_URL
celery.conf.result_backend = conf_settings.CELERY_CONF_RESULT_BACKEND


@celery.task(name="run_task")
def run_task(task_time :int):
    """
    Run task.
    :param task_time: Time give to sleep.
    """
    time.sleep(task_time)
    return True
