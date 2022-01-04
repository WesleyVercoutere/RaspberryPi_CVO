import asyncio

async def fct1():
    print("test1")
    await asyncio.sleep(1)
    print("test2")    

async def fct2():
    print("test3")
    await asyncio.sleep(1)
    print("test4")
    

async def main():
    print('test5')
    await asyncio.gather(
        fct1(),
        fct2()
        )   
    
    print('test6')

# Python 3.7+
asyncio.run(main())

# run roept main aan, await wacht 1 sec maar geeft python de vrijheid andere zaken te doen
#asyncio.gather(*aws, return_exceptions=False) Run awaitable objects in the aws sequence concurrently.
# If any awaitable in aws is a coroutine, it is automatically scheduled as a Task.
