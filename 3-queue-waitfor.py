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
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        try:
            # retrieve the get() awaitable
            get_await = queue.get()
            # await the awaitable with a timeout
            item = await asyncio.wait_for(get_await, 0.5)
        except asyncio.TimeoutError:
            print(f'{time.ctime()} Consumer: gave up waiting...')
            continue
        # check for stop
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
# Wed Aug 23 14:23:06 2023 Consumer: Running
# Wed Aug 23 14:23:07 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:07 2023 >got 0.5445749498885392
# Wed Aug 23 14:23:07 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:08 2023 >got 0.9359328115598423
# Wed Aug 23 14:23:08 2023 >got 0.11528308747914029
# Wed Aug 23 14:23:08 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:08 2023 >got 0.6833214801885751
# Wed Aug 23 14:23:08 2023 >got 0.07284418642457868
# Wed Aug 23 14:23:09 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:09 2023 >got 0.6641219793512918
# Wed Aug 23 14:23:09 2023 >got 0.4294578592146353
# Wed Aug 23 14:23:10 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:10 2023 >got 0.9786576645289532
# Wed Aug 23 14:23:11 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:11 2023 >got 0.600726144456646
# Wed Aug 23 14:23:12 2023 Consumer: gave up waiting...
# Wed Aug 23 14:23:12 2023 Producer: Done
# Wed Aug 23 14:23:12 2023 >got 0.8064092442594814
# Wed Aug 23 14:23:12 2023 Consumer: Done
#