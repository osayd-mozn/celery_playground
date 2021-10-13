from core.app import celery_app
from time import sleep


@celery_app.task(queue="io_queue", ack_late=True, ignore_result=True)
def busy_io_task(timeout, freq=1):
    busy_io_function(timeout, freq)
   

def busy_io_function(timout, freq):
    counter = 0
    while counter < timout:
        sleep(freq)
        counter += freq    
