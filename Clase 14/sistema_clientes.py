#Programa de consola para gestionar los clientes de una empresa, permitiendo agregar nuevos clientes, listar clientes, buscar clientes por ID, buscar clientes por nombre y eliminar clientes por ID.
import psycopg
from datetime import datetime

class Cliente:
    def __init__(self, id, nombre_completo, fecha_nacimiento, direccion, localidad_y_codigo_postal, telefono, email, fecha_registro, id_grupo_cliente):
        self.id = id
        self.nombre_completo = nombre_completo
        self.fecha_nacimiento = fecha_nacimiento
        self.direccion = direccion
        self.localidad_y_codigo_postal = localidad_y_codigo_postal
        self.telefono = telefono
        self.email = email
        self.fecha_registro = fecha_registro
        self.id_grupo_cliente = id_grupo_cliente
    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre_completo}, Fecha de Nacimiento: {self.fecha_nacimiento}, Dirección: {self.direccion}, Localidad y Código Postal: {self.localidad_y_codigo_postal}, Teléfono: {self.telefono}, Email: {self.email}, Fecha de Registro: {self.fecha_registro}, ID Grupo Cliente: {self.id_grupo_cliente}"
class ConexionBD:
    @staticmethod
    def conectar():
        try:
            conn = psycopg.connect(
                dbname='mi_base',
                user='postgres',
                password='ratonmalvado',
                host='localhost',
                port='5432'
            )
            return conn
        except Exception as e:
            print(f"Error al conectar a la base de datos: {e}")
            return None
    @staticmethod
    def insertar_datos(sql, params):
        conn = ConexionBD.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql, params)
                    conn.commit()
                    print("Datos insertados correctamente.")
            except Exception as e:
                print(f"Error al insertar datos: {e}")
            finally:
                conn.close()
    @staticmethod
    def leer_datos(sql):
        conn = ConexionBD.conectar()
        if conn:
            try:
                with conn.cursor() as cur:
                    cur.execute(sql)
                    rows = cur.fetchall()
                    return rows
            except Exception as e:
                print(f"Error al leer datos: {e}")
                return []
            finally:
                conn.close()
class SistemaClientes:
    def __init__(self):
        self.clientes = []
        self.cargar_clientes()

    def cargar_clientes(self):
        sql = "SELECT * FROM clientes;"
        rows = ConexionBD.leer_datos(sql)
        for row in rows:
            cliente = Cliente(*row)
            self.clientes.append(cliente)

    def agregar_cliente(self, cliente):
        sql = """
            INSERT INTO clientes (id, nombre_completo, fecha_nacimiento, direccion, localidad_y_codigo_postal, telefono, email, fecha_registro, id_grupo_cliente)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
        """
        params = (cliente.id, cliente.nombre_completo, cliente.fecha_nacimiento, cliente.direccion,
                  cliente.localidad_y_codigo_postal, cliente.telefono, cliente.email,
                  cliente.fecha_registro, cliente.id_grupo_cliente)
        ConexionBD.insertar_datos(sql, params)
        self.clientes.append(cliente)
    
    def obtener_sigiente_id(self):
        if not self.clientes:
            return '1'
        else:
            ultimo_id = max(int(c.id) for c in self.clientes)
            return ultimo_id + 1

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)

    def buscar_cliente_por_id(self, id):
        for cliente in self.clientes:
            if cliente.id == id:
                return cliente
        return None

    def buscar_cliente_por_nombre(self, nombre):
        resultados = []
        for cliente in self.clientes:
            if nombre.lower() in cliente.nombre_completo.lower():
                resultados.append(cliente)
        return resultados

    def eliminar_cliente_por_id(self, id):
        sql = "DELETE FROM clientes WHERE id = %s;"
        params = (id,)
        ConexionBD.insertar_datos(sql, params)
        self.clientes = [c for c in self.clientes if c.id != id]
if __name__ == "__main__":
    sistema = SistemaClientes()
    while True:
        print("\nSistema de Gestión de Clientes")
        print("1. Listar Clientes")
        print("2. Buscar Cliente por ID")
        print("3. Buscar Cliente por Nombre")
        print("4. Agregar Cliente")
        print("5. Eliminar Cliente por ID")
        print("6. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sistema.listar_clientes()
        elif opcion == '2':
            id_cliente = input("Ingrese el ID del cliente: ")
            cliente = sistema.buscar_cliente_por_id(id_cliente)
            if cliente:
                print(cliente)
            else:
                print("Cliente no encontrado.")
        elif opcion == '3':
            nombre_cliente = input("Ingrese el nombre del cliente: ")
            resultados = sistema.buscar_cliente_por_nombre(nombre_cliente)
            if resultados:
                for c in resultados:
                    print(c)
                    print("-----")
            else:
                print("No se encontraron clientes con ese nombre.")
        elif opcion == '4':
            id = sistema.obtener_sigiente_id()
            print(f"Nuevo ID generado: {id}")
            nombre_completo = input("Ingrese el nombre completo del cliente: ")
            fecha_nacimiento = input("Ingrese la fecha de nacimiento (YYYY-MM-DD): ")
            direccion = input("Ingrese la dirección del cliente: ")
            localidad_y_codigo_postal = input("Ingrese la localidad y código postal: ")
            telefono = input("Ingrese el teléfono del cliente: ")
            email = input("Ingrese el correo electrónico del cliente: ")
            fecha_registro = datetime.now().strftime("%Y-%m-%d")  # Fecha actual en formato YYYY-MM-DD
            id_grupo_cliente = input("Ingrese el ID del grupo de clientes: ")
            
            nuevo_cliente = Cliente(id, nombre_completo, fecha_nacimiento, direccion, 
                                    localidad_y_codigo_postal, telefono, email, 
                                    fecha_registro, id_grupo_cliente)
            sistema.agregar_cliente(nuevo_cliente)
        elif opcion == '5':
            id_cliente = input("Ingrese el ID del cliente a eliminar: ")
            sistema.eliminar_cliente_por_id(id_cliente)
        elif opcion == '6':
            break
        else:
            print("Opción no válida. Intente nuevamente.")
