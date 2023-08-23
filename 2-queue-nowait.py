from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    print(f'{time.ctime()} Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print(f'{time.ctime()} Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.5)
            continue
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
# Producer: Running
# Consumer: Running
# Wed Aug 23 14:16:49 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:49 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:50 2023 >got 0.7790762293227729
# Wed Aug 23 14:16:50 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:50 2023 >got 0.6840938234696025
# Wed Aug 23 14:16:50 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:51 2023 >got 0.5370406111262813
# Wed Aug 23 14:16:51 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:51 2023 >got 0.3035636107243922
# Wed Aug 23 14:16:51 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:52 2023 >got 0.6129737496735502
# Wed Aug 23 14:16:52 2023 >got 0.04109466874293022
# Wed Aug 23 14:16:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:52 2023 >got 0.5185898989123816
# Wed Aug 23 14:16:52 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:53 2023 >got 0.4875107636883259
# Wed Aug 23 14:16:53 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:53 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:54 2023 >got 0.5698020771523908
# Wed Aug 23 14:16:54 2023 Consumer: got nothing, waiting a while...
# Wed Aug 23 14:16:54 2023 Producer: Done
# Wed Aug 23 14:16:54 2023 >got 0.723046648570452
# Wed Aug 23 14:16:54 2023 Consumer: Done
#