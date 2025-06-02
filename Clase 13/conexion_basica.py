import psycopg


lista_estudiantes = [
    {"nombre": "Juan Pérez", "email": "juan.perez@example.com"},
    {"nombre": "Ana Gómez", "email": "ana.gomez@example.com"},
    {"nombre": "Carlos López", "email": "carlos.lopez@example.com"},
    {"nombre": "María Rodríguez", "email": "maria.rodriguez@example.com"},
    {"nombre": "Luis Fernández", "email": "luis.fernandez@example.com"}
]

     

#este codigo establece una conexión a una base de datos PostgreSQL
#y realiza una consulta simple para obtener datos de una tabla llamada "estudiantes".
with psycopg.connect("dbname=mi_base user=postgres password=ratonmalvado") as conn:
    with conn.cursor() as cur:
        # Ejecutar una consulta para obtener todos los registros de la tabla "estudiantes"
        cur.execute("SELECT * FROM estudiantes")
        for row in cur.fetchall():
            print(row)
        # Insertar un nuevo registro en la tabla "estudiantes"
        cur.execute("INSERT INTO estudiantes (nombre, correo) VALUES ('Alberto Martinez', 'albertma67@outlook.com')")
        # Insertando con parametros posicionales
        cur.execute("INSERT INTO estudiantes (nombre, correo) VALUES (%s, %s)", ('Florencia Vera', 'verflores995@gmail.com'))
        # Insertando con parametros nombrados
        cur.execute("INSERT INTO estudiantes (nombre, correo) VALUES (%(nombre)s, %(correo)s)", {'nombre': 'Marcos Lopez', 'correo': 'marloco56@yahoo.com'})
        # Insertando varios registros a la vez
        cur.executemany("INSERT INTO estudiantes (nombre, correo) VALUES (%(nombre)s, %(email)s)", lista_estudiantes)        
        # Confirmar los cambios en la base de datos
        conn.commit()
        # Volver a ejecutar la consulta para verificar los cambios
        cur.execute("SELECT * FROM estudiantes")
        for row in cur.fetchall():
            print(row)
