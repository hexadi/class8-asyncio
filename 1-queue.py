# we will create a producer coroutine that will generate ten random numbers 
# and put them on the queue. We will also create a consumer coroutine 
# that will get numbers from the queue and report their values.

from random import random
import asyncio
import time

# corountine to generate work
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
        print(f'{time.ctime()} Producer: put {value}')
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')
# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # check for stop signal
        if item is None:
            break
        # report
        print(f'{time.ctime()} >got {item}')
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))

# start the asyncio program
asyncio.run(main())

#
# Wed Aug 23 14:05:48 2023 Producer: Running
# Wed Aug 23 14:05:48 2023 Consumer: Running
# Wed Aug 23 14:05:49 2023 >got 0.9694193966927511
# Wed Aug 23 14:05:50 2023 >got 0.7935367758455517
# Wed Aug 23 14:05:50 2023 >got 0.2608187596014012
# Wed Aug 23 14:05:50 2023 >got 0.11137181663792128
# Wed Aug 23 14:05:50 2023 >got 0.14927166751874243
# Wed Aug 23 14:05:51 2023 >got 0.22385732121126856
# Wed Aug 23 14:05:51 2023 >got 0.6616725935541005
# Wed Aug 23 14:05:51 2023 >got 0.18832991023051837
# Wed Aug 23 14:05:52 2023 >got 0.3316689014267884
# Wed Aug 23 14:05:52 2023 Producer: Done
# Wed Aug 23 14:05:52 2023 >got 0.23073264062932286
# Wed Aug 23 14:05:52 2023 Consumer: Done
#