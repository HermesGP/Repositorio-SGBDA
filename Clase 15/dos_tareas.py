import asyncio

async def tarea1():
    print("Tarea 1 iniciada")
    await asyncio.sleep(3)
    print("Tarea 1 finalizada")

async def tarea2():
    print("Tarea 2 iniciada")
    await asyncio.sleep(1)
    print("Tarea 2 finalizada")

async def main():
    await asyncio.gather(tarea1(), tarea2())
asyncio.run(main())
