#Script para cargar en la base de datos datos sobre un producto escritos por el usuario en la consola.
import psycopg
from decimal import Decimal
#esta función solicita al usuario un número y verifica que sea válido.
def numero_valido(mensaje):
    while True:
        try:
            valor = Decimal(input(mensaje))
            if valor < 0:
                raise ValueError("El valor no puede ser negativo.")
            return valor
        except ValueError:
            print("El valor ingresado no es un número válido. Inténtelo de nuevo.")
# Esta función solicita al usuario una cadena de texto y verifica que no esté vacía.
def cadena_valida(mensaje):
    while True:
        valor = input(mensaje)
        if valor.strip() == "":
            print("El valor no puede estar vacío. Inténtelo de nuevo.")
        else:
            return valor.strip()
        
if __name__ == "__main__":
    lista_productos = []
    # Este script permite al usuario ingresar datos de productos y almacenarlos en una base de datos PostgreSQL.
    while True:
        # Solicitar datos del producto
        nombre = cadena_valida("Ingrese el nombre del producto: ")
        precio = numero_valido("Ingrese el precio del producto: ")
        cantidad = numero_valido("Ingrese la cantidad del producto: ")
        categoria = cadena_valida("Ingrese la categoría del producto: ")
        # Colocar los datos en una lista de diccionarios
        producto = {
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad,
            "categoria": categoria
        }
        lista_productos.append(producto)

        # Preguntar si se desea continuar
        continuar = input("¿Desea ingresar otro producto? (s/n): ").strip().lower()
        if continuar != 's':
            print("Proceso de carga de productos finalizado.")
            break

    # Conectar a la base de datos y realizar la inserción
    with psycopg.connect("dbname=mi_base user=postgres password=ratonmalvado") as conn:
        with conn.cursor() as cur:
            for producto in lista_productos:
                try:
                    cur.execute(
                        "INSERT INTO productos (nombre, precio, cantidad, categoria) VALUES (%(nombre)s, %(precio)s, %(cantidad)s,%(categoria)s)",
                            producto
                    )
                    conn.commit()
                except Exception as e:
                    print(f"Error al insertar el producto: {e}")
                    # Si ocurre un error, revertir la transacción
                    conn.rollback()
                    continue
                else:
                    print(f"Producto '{producto['nombre']}' insertado correctamente.")
            # Verificar los datos insertados
            cur.execute("SELECT * FROM productos")
