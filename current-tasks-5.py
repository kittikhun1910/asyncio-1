# example of waiting for all tasks to complete
import random
import asyncio
import time

# corotine to execute in a new task


async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random.random()
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f'{time.ctime()} >task {arg} done with {value}')

# main corotine


async def main():
    # create many task
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete #ALL_COMPLETED, FIRST_COMPLETED, FIRST_EXCEPTION
    done, pending = await asyncio.wait(tasks, return_when=asyncio.ALL_COMPLETED)
    # report result
    print(f'{time.ctime()} All done')

# start the asyncio program
asyncio.run(main())

# Wed Jul 12 15:02:54 2023 >task 7 done with 0.07677905254516781
# Wed Jul 12 15:02:54 2023 >task 8 done with 0.20098971488966078
# Wed Jul 12 15:02:55 2023 >task 1 done with 0.3216550426287813
# Wed Jul 12 15:02:55 2023 >task 6 done with 0.3603618321407719
# Wed Jul 12 15:02:55 2023 >task 2 done with 0.4004648584896847
# Wed Jul 12 15:02:55 2023 >task 4 done with 0.5454365668970401
# Wed Jul 12 15:02:55 2023 >task 3 done with 0.5970906669334896
# Wed Jul 12 15:02:55 2023 >task 5 done with 0.6284520020124846
# Wed Jul 12 15:02:55 2023 >task 0 done with 0.7744320168853358
# Wed Jul 12 15:02:55 2023 >task 9 done with 0.9412743218754928
# Wed Jul 12 15:02:55 2023 All done