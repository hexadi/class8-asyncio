from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print(f'{time.ctime()} Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        if item:
            await asyncio.sleep(item)
        # mark the task as done
        queue.task_done()

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # start the producer and wait for it to finish
    await asyncio.create_task(producer(queue))
    # wait for all items to be processed
    await queue.join()

#start the asyncio program
asyncio.run(main())

#
# Wed Aug 23 14:29:17 2023 Consumer: Running
# Wed Aug 23 14:29:17 2023 Producer: Running
# Wed Aug 23 14:29:17 2023 >got 0.05383185223760811
# Wed Aug 23 14:29:18 2023 >got 0.7312024645181848
# Wed Aug 23 14:29:19 2023 >got 0.9292012307369238
# Wed Aug 23 14:29:20 2023 >got 0.9906341353911791
# Wed Aug 23 14:29:21 2023 >got 0.13205029165459603
# Wed Aug 23 14:29:21 2023 >got 0.5800810458941529
# Wed Aug 23 14:29:22 2023 >got 0.8419437507968337
# Wed Aug 23 14:29:23 2023 >got 0.09751608282608204
# Wed Aug 23 14:29:23 2023 Producer: Done
# Wed Aug 23 14:29:23 2023 >got 0.8547325236461065
# Wed Aug 23 14:29:24 2023 >got 0.06329010503180788
#