from core.app import celery_app
import signal


def handler(*args, **kwargs):
    raise ValueError("Timeout is reached")


signal.signal(signal.SIGALRM, handler)


@celery_app.task(queue="cpu_queue", ack_late=True, ignore_result=True)
def busy_cpu_task(timeout, succeed=True):
    signal.alarm(timeout)
    try:
        busy_cpu_function()
    except ValueError as e:
        if not succeed:
            raise e


def busy_cpu_function():
    c = 0
    while True:
        c += 1
        if c == 1e1000:
            break
        # if c % 500 == 0:
        #     print(f"c: {c}")