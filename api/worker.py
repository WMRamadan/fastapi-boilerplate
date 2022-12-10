"""Celery worker."""
#--------------------------------------------#
# PEP-8 Imports Priority.
# 1.Standard Library Imports
# 2.Related Library Imports
# 3.Local application/library imports
#--------------------------------------------#
import time
from celery import Celery


celery = Celery(__name__)
celery.conf.broker_url = "redis://localhost:6379"
celery.conf.result_backend = "redis://localhost:6379"


@celery.task(name="run_task")
def run_task(task_time :int):
    """
    Run task.
    :param task_time: Time give to sleep.
    """
    time.sleep(task_time)
    return True
