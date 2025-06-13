import aiohttp
import asyncio

async def solicitud(url):
    async with aiohttp.ClientSession() as sesion:
        async with sesion.get(url) as respuesta:
            return await respuesta.text()
async def main():
    url = "http://httpbin.org/get"
    resultado = await solicitud(url)
    print(resultado)
if __name__ == "__main__":
    asyncio.run(main())
