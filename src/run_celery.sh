#! /usr/bin/env bash
celery \
--app=core.app.celery_app \
--result-backend=redis://:@redis:6379/0 \
worker \
--loglevel=info \
--queues=cpu_queue,io_queue \
--prefetch-multiplier=100 \
--pool=prefork \
-c 1 \
-n worker_${HOSTNAME}