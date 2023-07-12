# example of gather for many corotines in a list
import asyncio
import time

# corotine use for a task


async def task_coro(value):
    # report a message
    print(f'{time.ctime()} task {value} executing')
    # sleep for a moment
    await asyncio.sleep(1)

# coroutine used for the entry point


async def main():
    # report a message
    print(f'{time.ctime()} main starting.')
    # create many coroutines
    coros = [task_coro(i) for i in range(10)]
    # run the tasks
    await asyncio.gather(*coros)
    # report a message
    print(f'{time.ctime()} main done')

# start the asyncio program
asyncio.run(main())

# Wed Jul 12 14:55:00 2023 main starting.
# Wed Jul 12 14:55:00 2023 task 0 executing
# Wed Jul 12 14:55:00 2023 task 1 executing
# Wed Jul 12 14:55:00 2023 task 2 executing
# Wed Jul 12 14:55:00 2023 task 3 executing
# Wed Jul 12 14:55:00 2023 task 4 executing
# Wed Jul 12 14:55:00 2023 task 5 executing
# Wed Jul 12 14:55:00 2023 task 6 executing
# Wed Jul 12 14:55:00 2023 task 7 executing
# Wed Jul 12 14:55:00 2023 task 8 executing
# Wed Jul 12 14:55:00 2023 task 9 executing
# Wed Jul 12 14:55:01 2023 main done