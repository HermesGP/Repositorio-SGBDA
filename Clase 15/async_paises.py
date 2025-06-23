import aiohttp
import asyncio
import psycopg
async def solicitar_pais(sesion, url):
    async with sesion.get(url) as respuesta:
        try:
            datos = await respuesta.json()
            return datos
        except Exception as ex:
            print(f"Error en la solicitud: {ex}")
async def solicitar_lista_paises(paises):
    async with aiohttp.ClientSession() as sesion:
        tareas = []
        for pais in paises:
            url = f"https://restcountries.com/v3.1/translation/{pais}"
            tarea = solicitar_pais(sesion, url)
            tareas.append(tarea)
        resultados = await asyncio.gather(*tareas)
        return resultados
def filtrar_datos(datos):   
    datos_paises = [] 
    for pais in datos:
        datos_paises.append({
            "nombre": pais[0]["translations"]["spa"]["common"],
            "capital": pais[0]["capital"][0],
            "region": pais[0]["region"],
            "subregion": pais[0]["subregion"],
            "poblacion": pais[0]["population"],
            "area": pais[0]["area"],
            "bandera": pais[0]["flags"]["png"]
        })
    return datos_paises
async def insertar_datos(datos):
    try:
        async with await psycopg.AsyncConnection.connect(
                    dbname='mi_base',
                    user='postgres',
                    password='ratonmalvado',
                    host='localhost',
                    port='5432'
        ) as aconn:
            async with aconn.cursor() as acur:
                await acur.execute(
                    "INSERT INTO paises (nombre, capital, region, subregion, poblacion, area, bandera) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (datos["nombre"], datos["capital"], datos["region"], datos["subregion"], datos["poblacion"], datos["area"], datos["bandera"])
                )
    except Exception as ex:
        print(f"Error en la comunicacion con la base de datos: {ex}")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    paises = ["suiza", "alemania", "paraguay", "argentina", "italia"]
    datos = asyncio.run(solicitar_lista_paises(paises))
    datos_paises = filtrar_datos(datos)
    for pais in datos_paises:
        asyncio.run(insertar_datos(pais))