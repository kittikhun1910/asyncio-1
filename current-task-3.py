# example of starting many tasks and getting access to all tasks
import asyncio
import time

# coroutine for a task


async def task_coroutine(value):
    # report a massage
    print(f'{time.ctime()} task {value} is running')
    # block for a moment
    await asyncio.sleep(1)

# define a main coroutine


async def main():
    # report a massage
    print(f'{time.ctime()} main coroutine started')
    # start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i)) for i in range(10)]
    # allow some of the tasks time to start
    await asyncio.sleep(0.1)
    # get all tasks
    tasks = asyncio.all_tasks()
    # report all tasks
    for task in tasks:
        print(f'{time.ctime} > {task.get_name()}, {task.get_coro}')
    # wait for all tasks to complete
    for task in started_tasks:
        await task

# start the asyncio program
asyncio.run(main())

# Wed Jul 12 14:36:54 2023 main coroutine started
# Wed Jul 12 14:36:54 2023 task 0 is running
# Wed Jul 12 14:36:54 2023 task 1 is running
# Wed Jul 12 14:36:54 2023 task 2 is running
# Wed Jul 12 14:36:54 2023 task 3 is running
# Wed Jul 12 14:36:54 2023 task 4 is running
# Wed Jul 12 14:36:54 2023 task 5 is running
# Wed Jul 12 14:36:54 2023 task 6 is running
# Wed Jul 12 14:36:54 2023 task 7 is running
# Wed Jul 12 14:36:54 2023 task 8 is running
# Wed Jul 12 14:36:54 2023 task 9 is running
# <built-in function ctime> > Task-6, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63A00>
# <built-in function ctime> > Task-9, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63C40>
# <built-in function ctime> > Task-4, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63880>
# <built-in function ctime> > Task-3, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD637C0>
# <built-in function ctime> > Task-1, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD628C0>
# <built-in function ctime> > Task-7, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63AC0>
# <built-in function ctime> > Task-2, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63700>
# <built-in function ctime> > Task-10, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63D00>
# <built-in function ctime> > Task-5, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63940>
# <built-in function ctime> > Task-8, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63B80>
# <built-in function ctime> > Task-11, <built-in method get_coro of _asyncio.Task object at 0x0000017E6AD63DC0>