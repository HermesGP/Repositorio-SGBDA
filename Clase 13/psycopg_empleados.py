import psycopg
from decimal import Decimal

def cargar_datos():
    nombre = input("Escriba su nombre: ")
    edad = int(input("Escriba su edad: "))
    email = input("Escriba su email: ")
    cargo = input("Escriba su cargo: ")
    salario = Decimal(input("Escriba su salario: "))
    empleado = {
        "nombre": nombre,
        "edad": edad,
        "email": email,
        "cargo": cargo,
        "salario": salario
    }
    return empleado
if __name__ == "__main__":
    empleado = cargar_datos()
    with psycopg.connect("dbname=mi_base user=postgres password=ratonmalvado") as con:
        with con.cursor() as cur:
            try:
                cur.execute(
                    """INSERT INTO empleados (nombre, edad, email, cargo, salario)
                    VALUES(%(nombre)s, %(edad)s, %(email)s, %(cargo)s, %(salario)s)""",
                    empleado
                )
                con.commit()
            except Exception as e:
                print(f"Error al insertar los datos: {e}")
                con.rollback()
            else:
                print(f"Empleado '{empleado["nombre"]}' insertado correctamente")
            cur.execute("SELECT * from empleados")
            for fila in cur.fetchall():
                print(fila)
        