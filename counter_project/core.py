from __future__ import absolute_import
from counter_project.celery import app
from counter_project.counter import Counter
import local_settings
import redis

config = local_settings.env
redis_database = redis.Redis(host=config.get('MESSAGE_BROKER'), port=6379) 
counter = Counter(redis_database)

@app.task
def request_counter():
    return counter.get()

@app.task
def modify_counter():
    ascending = counter.check_ascending()
    if ascending:
        counter.increase()
    else:
        counter.decrease()
