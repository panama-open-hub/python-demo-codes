import time
import asyncio

start = time.time()


def tic():
    return 'at %1.1f seconds' % (time.time() - start)

async def runBg():
    while True:
        print("from background {}".format(tic()))
        #time.sleep(.5)
        await asyncio.sleep(0.5)

async def runMain():
    for i in range(5):
        print("from main {}".format(tic()))
        #time.sleep(1)
        await asyncio.sleep(1)



async def main():
    tasks = [runBg(), runMain()]
    await asyncio.gather(*tasks)


asyncio.run(main())