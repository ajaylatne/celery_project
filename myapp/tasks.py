from celery import shared_task
from time import sleep


@shared_task
def sub(x, y):
    sleep(5)
    return x - y


# periodic task
@shared_task
def clear_session_cache():
    print('clear session cache')
    return 'Done'
