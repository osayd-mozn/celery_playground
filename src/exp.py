from core.io_task import busy_io_task
from core.cpu_task import busy_cpu_task


def main():
    for i in range(2):
        timeout = 180
        # if i % 2 == 0 and i <= 15:
        #     timeout = 600
        # task_id = busy_io_task.delay(timeout=timeout, freq=2)
        task_id = busy_cpu_task.delay(timeout=timeout)
    print(f"task is submitted with id {task_id}")


if __name__ == "__main__":
    main()
