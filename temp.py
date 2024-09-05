# SuperFastPython.com
# example of waiting for all tasks to complete
from random import random, randint, randrange
import asyncio


# coroutine to execute in a new task
async def task_coro(arg):
    # generate a random value between 0 and 1
    value = random() if arg % 2 == 0 else randrange(1, 10)
    # block for a moment
    await asyncio.sleep(value)
    # report the value
    print(f">task {arg} done with {value}")

    return randint(1, 100), randint(50, 100)


# main coroutine
async def main():
    # create many tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(10)]
    # wait for all tasks to complete
    done, pending = await asyncio.wait(tasks, timeout=1)
    # report results
    print("All done")
    print(f"{done=}")
    print(f"{pending=}")

    for c in done:
        print(f"{c.get_name()}: {c.result()=} : {c.cancelled() = }")

    for c in pending:
        print(f"{c.get_name()}: {c.done()=} : {c.cancelled() = }")

        print(f"{c._state = }")


# start the asyncio program
asyncio.run(main())
