import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования.")
    for i in range(1, 6):
        await asyncio.sleep(1 / power)
        print(f"Силач {name} поднял {i} шар.")
    print(f"Силач {name} закончил соревнования.")

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Ruslan', 3)),
        asyncio.create_task(start_strongman('Sergey', 6)),
        asyncio.create_task(start_strongman('George', 9)),
    ]
    for task in tasks:
        await task

asyncio.run(start_tournament())