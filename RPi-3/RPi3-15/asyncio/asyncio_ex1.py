import asyncio

# opmerking verander sleep tijden in fct1 en fct2 

async def fct1():
    print("test1")
    await asyncio.sleep(3)
    print("test2")    

async def fct2():
    print("test3")
    await asyncio.sleep(2)
    print("test4")
    

async def main():
    print('test5')
    task1 = asyncio.create_task(fct1())
    task2 = asyncio.create_task(fct2())    
    await task1 # 1 await is voldoende om alle tasks te starten!!! zet maar 1vd 2 in commentaar
    print("X")
    await task2 # 1 await is niet voldoende om alle taken te laten eindigen!!!  als taak 1 sneller is dan wacht men niet op taak 2 
    print("Y")    
    print('test6')

# Python 3.7+
asyncio.run(main())

# run roept main aan, await wacht 1 sec maar geeft python de vrijheid andere zaken te doen