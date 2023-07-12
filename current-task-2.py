# example of getting the current task from the main coroutien
import asyncio
import time

# define a main coroutine


async def main():
    # report a massage
    print(f'{time.ctime()} main coroutine started ')
    # get the current task
    task = asyncio.current_task()
    # report its detail
    print(f'{time.ctime()}{task}')

# start the asyncio programs

asyncio.run(main())

# Wed Jul 12 14:22:11 2023 main coroutine started
# Wed Jul 12 14:22:11 2023<Task pending name='Task-1' coro=<main() running at D:\work_23-1\code-asyn\asyncio-1\current-task-1.py:14>
# cb=[_run_until_complete_cb() at C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.11_3.11.1264.0_x64__qbz5n2kfra8p0\Lib\asyncio\base_events.py:180]>
