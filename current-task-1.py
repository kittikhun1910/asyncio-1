# example of getting the current task from the main coroutien
import asyncio

# define a main coroutine


async def main():
    # report a massage
    print('main coroutine started')
    # get the current task
    task = asyncio.current_task()
    # report its detail
    print(task)

# start the asyncio programs
asyncio.run(main())
