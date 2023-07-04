import asyncio
from utils import async_timed

async def sleepCoro(sleepTime=10):
    print("Entering sleepCoro and sleeping ")
    await asyncio.sleep(sleepTime)
    print("Finished sleepCoro, Exiting")

async def someBusyTask(sleepTime=2, instanceName=""):
    while True:
        print(f"Starting sleep cycle in someBusyTask instance {instanceName} ")
        await asyncio.sleep(sleepTime)
        print(f"Finished sleep cycle in SomeBusyTask {instanceName}")


async def main():
    coro=await sleepCoro()
    tsk1= asyncio.create_task(someBusyTask(2, "instance 1"))
    tsk2= asyncio.create_task(someBusyTask(2, "instance 2"))
    tsks=[tsk1, tsk2]
    await asyncio.tasks.wait(tsks)
    
asyncio.run(main())