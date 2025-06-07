#script para cargar una lista de clientes desde un archivo xlsx en una base de datos postgresql
#primero cargando en un dataframe de pandas 
import pandas as pd
import psycopg
try:
    # Cargar el archivo Excel en un DataFrame
    df = pd.read_excel('C:\\Users\\herme\\Repositorio SGBDA\\Clase 14\\clientes.xlsx')
    print("Archivo cargado correctamente.")
except FileNotFoundError:
    print("El archivo no existe.")
    exit()
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
    exit()
print(df.head(10))
#corregir direcciones mal cargadas, intercambiando los valores de las columnas direccion y localidad cuando la direccion es Londres
df.loc[df['Dirección'] == 'London', ['Dirección', 'Localidad y Código postal']] = df.loc[df['Dirección'] == 'London', ['Localidad y Código postal', 'Dirección']].values
print("Direcciones corregidas.")
#imprimir al cliente con id C0481 para verificar que se ha corregido la direccion
print(df[df['ID'] == 'C0481'])
#Cambiar los valores de la columna 'Grupo de clientes' a números enteros
mapeo_grupos = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
}
df['Grupo de clientes'] = df['Grupo de clientes'].map(mapeo_grupos)
# Imprimir el DataFrame para verificar los cambios
print(df.head(10))
# Abrir una conexión a la base de datos PostgreSQL con with para asegurar el cierre de la conexión
with psycopg.connect(
    dbname='mi_base',
    user='postgres',
    password='ratonmalvado',
    host='localhost',
    port='5432'
) as conn:
    with conn.cursor() as cur:
        # Insertar los datos del DataFrame en la tabla clientes
        for index, row in df.iterrows():
            cur.execute("""
                INSERT INTO clientes (nombre_completo, fecha_nacimiento, direccion, localidad_y_codigo_postal, telefono, email, fecha_registro, id_grupo_cliente)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
            """, (row['Nombre completo'], row['Fecha de nacimiento'], row['Dirección'], row['Localidad y Código postal'], row['Teléfono'], row['Correo electrónico'], row['Fecha de alta'], row['Grupo de clientes']))
        # Confirmar los cambios
        conn.commit()
        print("Datos insertados correctamente en la base de datos.")
        # Realizar una consulta para verificar los datos insertados
        cur.execute("SELECT * FROM clientes;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    


    

