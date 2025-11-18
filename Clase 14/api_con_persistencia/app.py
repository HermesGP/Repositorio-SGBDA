from flask import Flask
from routes import routes
from data import conexion_db, crear_tabla_usuarios, cargar_datos_iniciales

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == '__main__':
    # Crear conexión y tabla al iniciar la aplicación
    conn = conexion_db()
    if conn:
        crear_tabla_usuarios(conn)
        cargar_datos_iniciales(conn)
    app.run(debug=True)