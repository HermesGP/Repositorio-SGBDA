#Cargar los datos del dataset titanic.csv en un dataframe de pandas, filtrarlos y guardarlos en una base de datos PostgreSQL.
import pandas as pd
import psycopg
# Cargar el dataset
try:
    df = pd.read_csv("C:\\Users\\herme\\Repositorio SGBDA\\Clase 14\\titanic.csv", sep=',', encoding='utf-8')
except FileNotFoundError:
    print("El archivo no existe")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")
else:
    print("Archivo cargado correctamente.")
# Filtrar las columnas que nos interesan
df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age']]
#Convertir la columna survived a boolean
df['Survived'] = df['Survived'].astype(bool)
#Cambiar en español los valores de la columna sex
df.loc[df['Sex'] == 'male', 'Sex'] = 'masculino'
df.loc[df['Sex'] == 'female', 'Sex'] = 'femenino'
# Abrir una conexión a la base de datos PostgreSQL con with para asegurar el cierre de la conexión
with psycopg.connect(
    dbname='mi_base',
    user='postgres',
    password='ratonmalvado',
    host='localhost',
    port='5432'
) as conn:
    with conn.cursor() as cur:
        #Insertar los datos del DataFrame en la tabla
        for index, row in df.iterrows():
            cur.execute("""
                INSERT INTO titanic (numero_pasajero, supervivencia, clase_id, nombre, sexo, edad)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (row['PassengerId'], row['Survived'], row['Pclass'], row['Name'], row['Sex'], row['Age']))
        # Confirmar los cambios
        conn.commit()
        print("Datos insertados correctamente en la base de datos.")
        # Realizar una consulta para verificar los datos insertados
        cur.execute("SELECT t.nombre, t.sexo, t.edad, c.clase_nombre, t.supervivencia FROM titanic AS t JOIN clases_titanic AS c ON t.clase_id=c.clase_id;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
# Cerrar la conexión
# La conexión se cierra automáticamente al salir del bloque with
