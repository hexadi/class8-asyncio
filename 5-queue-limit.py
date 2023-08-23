from random import random
import asyncio
import time

# coroutine to generate work
async def producer(queue,id):
    time_start = time.ctime()
    print(f'{time_start} Producer {id}: Running')
    # generate work
    for i in range(10):
        # generate a value
        value = random()
        # block to simulate work
        await asyncio.sleep(id*0.1)
        # add to the queue
        await queue.put(value)
    time_done = time.ctime()
    print(f'{time_done} Producer {id}: Done')

# coroutine to consume work
async def consumer(queue):
    print(f'{time.ctime()} Consumer: Running')
    # consume work
    while True:
        # get a unit of work
        item = await queue.get()
        # report
        print(f'{time.ctime()} >got {item}')
        # block while processing
        if item:
            await asyncio.sleep(item)
        # mark as completed
        queue.task_done()
    # all done
    print(f'{time.ctime()} Consumer: Done')

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue(2)
    # start the consumer
    _ = asyncio.create_task(consumer(queue))
    # create many producers
    producers = [producer(queue,id) for id in range(1,6)]
    # run and wait for the producers to finish
    await asyncio.gather(*producers)
    # wait for the consumer to process all items
    await queue.join()

# start the asyncio program
asyncio.run(main())

#
# Wed Aug 23 14:34:05 2023 Consumer: Running
# Wed Aug 23 14:34:05 2023 Producer: Running
# Wed Aug 23 14:34:05 2023 Producer: Running
# Wed Aug 23 14:34:05 2023 Producer: Running
# Wed Aug 23 14:34:05 2023 Producer: Running
# Wed Aug 23 14:34:05 2023 Producer: Running
# Wed Aug 23 14:34:05 2023 >got 0.06359791468973164
# Wed Aug 23 14:34:05 2023 >got 0.14550064770365723
# Wed Aug 23 14:34:06 2023 >got 0.05108140141075401
# Wed Aug 23 14:34:06 2023 >got 0.38576029391331346
# Wed Aug 23 14:34:06 2023 >got 0.42983671962646963
# Wed Aug 23 14:34:06 2023 >got 0.6376399407100399
# Wed Aug 23 14:34:07 2023 >got 0.6005962829284311
# Wed Aug 23 14:34:08 2023 >got 0.6940359388960833
# Wed Aug 23 14:34:08 2023 >got 0.06630695568242273
# Wed Aug 23 14:34:08 2023 >got 0.011465665484887588
# Wed Aug 23 14:34:09 2023 >got 0.6362417346097649
# Wed Aug 23 14:34:09 2023 >got 0.41587482499510653
# Wed Aug 23 14:34:10 2023 >got 0.29157376846998484
# Wed Aug 23 14:34:10 2023 >got 0.41823895283500023
# Wed Aug 23 14:34:10 2023 >got 0.15190507864038738
# Wed Aug 23 14:34:10 2023 >got 0.3562691321303756
# Wed Aug 23 14:34:11 2023 >got 0.5181239760343092
# Wed Aug 23 14:34:11 2023 >got 0.9429463949726195
# Wed Aug 23 14:34:12 2023 >got 0.6816381690668216
# Wed Aug 23 14:34:13 2023 >got 0.2886520187653283
# Wed Aug 23 14:34:13 2023 >got 0.8853644928045384
# Wed Aug 23 14:34:14 2023 >got 0.3154968012098568
# Wed Aug 23 14:34:14 2023 >got 0.08611763252763394
# Wed Aug 23 14:34:15 2023 >got 0.914889986764538
# Wed Aug 23 14:34:15 2023 >got 0.7279072307736598
# Wed Aug 23 14:34:16 2023 >got 0.23464533980731084
# Wed Aug 23 14:34:16 2023 >got 0.2833991089082122
# Wed Aug 23 14:34:17 2023 >got 0.6659012936357279
# Wed Aug 23 14:34:17 2023 >got 0.2529209516328349
# Wed Aug 23 14:34:18 2023 >got 0.09662137028450901
# Wed Aug 23 14:34:18 2023 >got 0.8801706103424907
# Wed Aug 23 14:34:19 2023 >got 0.27167939517941664
# Wed Aug 23 14:34:19 2023 >got 0.23538202573587763
# Wed Aug 23 14:34:19 2023 >got 0.7382076167070007
# Wed Aug 23 14:34:20 2023 >got 0.4282407166972212
# Wed Aug 23 14:34:20 2023 >got 0.2684400661693006
# Wed Aug 23 14:34:20 2023 Producer: Done
# Wed Aug 23 14:34:21 2023 >got 0.2656036746842917
# Wed Aug 23 14:34:21 2023 >got 0.4736211935526372
# Wed Aug 23 14:34:21 2023 >got 0.23180983547511091
# Wed Aug 23 14:34:21 2023 >got 0.7964443105319173
# Wed Aug 23 14:34:22 2023 >got 0.5981032872962563
# Wed Aug 23 14:34:23 2023 >got 0.473101138836566
# Wed Aug 23 14:34:23 2023 >got 0.10853122074437727
# Wed Aug 23 14:34:23 2023 Producer: Done
# Wed Aug 23 14:34:23 2023 >got 0.05747173227855129
# Wed Aug 23 14:34:24 2023 >got 0.6971210698064965
# Wed Aug 23 14:34:24 2023 >got 0.2586349216163679
# Wed Aug 23 14:34:24 2023 Producer: Done
# Wed Aug 23 14:34:24 2023 >got 0.3415352768215295
# Wed Aug 23 14:34:24 2023 Producer: Done
# Wed Aug 23 14:34:25 2023 >got 0.16073810651143083
# Wed Aug 23 14:34:25 2023 Producer: Done
# Wed Aug 23 14:34:25 2023 >got 0.5532842140246148
# Wed Aug 23 14:34:26 2023 >got 0.773016052232419
#