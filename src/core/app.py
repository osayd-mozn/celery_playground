from celery import Celery
import os


# Here is a list of some configs we can use
# https://docs.celeryproject.org/en/stable/userguide/configuration.html#new-lowercase-settings
celery_app = Celery(
    "worker",
    broker=f"amqp://{os.getenv('RABBITMQ_DEFAULT_USER')}:{os.getenv('RABBITMQ_DEFAULT_PASS')}@queue//",
    backend="redis://:@redis:6379/0",
    include=["core.cpu_task", "core.io_task"],
    heartbeat=0,
)

celery_app.conf.task_routes = {
    # Screen Tasks
    "core.cup_task.busy_cpu_task": {"queue": "cpu_queue"},
    "core.io_task.busy_io_task": {"queue": "io_queue"}, 
}
