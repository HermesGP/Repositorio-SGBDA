import psycopg
from models import Usuario

def conexion_db():
    try:
        conn = psycopg.connect(
            dbname="mi_base",
            user="postgres",
            password="ratonmalvado",
            host="localhost",
            port="5432"
        )
        print("Conexión exitosa a la base de datos.")
        return conn
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tabla_usuarios(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            DROP TABLE IF EXISTS usuarios;
            CREATE TABLE usuarios (
                id SERIAL PRIMARY KEY,
                nombre VARCHAR(100),
                cedula VARCHAR(20),
                correo_electronico VARCHAR(100),
                telefono VARCHAR(15),
                fecha_nacimiento DATE
            );
        """)
        conn.commit()
        cursor.close()
        print("Tabla 'usuarios' creada o ya existe.")
    except Exception as e:
        print(f"Error al crear la tabla: {e}")

def cargar_datos_iniciales(conn):
    usuarios_iniciales = [
        Usuario(None, "Juan Perez", "123456789", "juan.perez@example.com", "555-1234", "1990-01-01"),
        Usuario(None, "Maria Gomez", "987654321", "maria.gomez@example.com", "555-5678", "1985-05-15"),
        Usuario(None, "Luis Rodriguez", "456789123", "luis.rodriguez@example.com", "555-8765", "1992-10-30"),
        Usuario(None, "Juan Martinez", "321654987", "juan.martinez@example.com", "555-4321", "1988-03-22"),
        Usuario(None, "Ana Gomez", "654987321", "ana.gomez@example.com", "555-1357", "1995-07-15")
    ]
    for usuario in usuarios_iniciales:
        insertar_usuario(conn, usuario)

def leer_tabla_usuarios(conn):
    usuarios = []
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, cedula, correo_electronico, telefono, fecha_nacimiento FROM usuarios;")
        rows = cursor.fetchall()
        for row in rows:
            usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
            usuarios.append(usuario)
        cursor.close()
    except Exception as e:
        print(f"Error al leer la tabla: {e}")
    return usuarios

def insertar_usuario(conn, usuario):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO usuarios (nombre, cedula, correo_electronico, telefono, fecha_nacimiento)
            VALUES (%s, %s, %s, %s, %s) RETURNING id;
        """, (usuario.nombre, usuario.cedula, usuario.correo_electronico, usuario.telefono, usuario.fecha_nacimiento))
        usuario.id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        print(f"Usuario {usuario.nombre} insertado con ID {usuario.id}.")
    except Exception as e:
        print(f"Error al insertar el usuario: {e}")

def buscar_por_nombre(conn, nombre):
    usuarios_encontrados = []
    try:
        cursor = conn.cursor()
        nombre = nombre.strip().lower()
        # Búsqueda por coincidencias parciales (insensible a mayúsculas/minúsculas)
        cursor.execute("SELECT id, nombre, cedula, correo_electronico, telefono, fecha_nacimiento FROM usuarios WHERE nombre LIKE %s;", (f"%{nombre}%",))
        rows = cursor.fetchall()
        for row in rows:
            usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
            usuarios_encontrados.append(usuario)
        cursor.close()
    except Exception as e:
        print(f"Error al buscar por nombre: {e}")
    return usuarios_encontrados

def actualizar_usuario_por_id(conn, id):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id = %s;", (id,))
        row = cursor.fetchone()
        if row:
            usuario = Usuario(row[0], row[1], row[2], row[3], row[4], row[5])
            cursor.close()
            return usuario
        cursor.close()
    except Exception as e:
        print(f"Error al buscar por ID: {e}")
    return None

def borrar_usuario_por_id(conn, id):
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = %s;", (id,))
        conn.commit()
        cursor.close()
        print(f"Usuario con ID {id} eliminado.")
    except Exception as e:
        print(f"Error al borrar el usuario: {e}")
