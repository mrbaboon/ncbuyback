import os
from celery import Celery
from celery.app import trace
from celery.signals import setup_logging

# set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ncbuyback.settings")

from django.conf import settings  # noqa

app = Celery("ncbuyback")

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings")


@setup_logging.connect
def config_loggers(*args, **kwargs):
    from logging.config import dictConfig  # noqa
    from django.conf import settings  # noqa

    dictConfig(settings.LOGGING)


# setup priorities ( 0 Highest, 9 Lowest )
app.conf.broker_transport_options = {
    "priority_steps": list(range(10)),  # setup que to have 10 steps
    "queue_order_strategy": "priority",  # setup que to use prio sorting
}
app.conf.task_default_priority = 5  # anything called with the task.delay() will be given normal priority (5)
app.conf.worker_prefetch_multiplier = 1  # only prefetch single tasks at a time on the workers so that prio tasks happen

app.conf.ONCE = {
    "backend": "eveuniverse.backends.DjangoBackend",
    "settings": {},
}

app.conf.ONCE = {"backend": "allianceauth.services.tasks.DjangoBackend", "settings": {}}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# Remove result from default log message on task success
trace.LOG_SUCCESS = "Task %(name)s[%(id)s] succeeded in %(runtime)ss"
