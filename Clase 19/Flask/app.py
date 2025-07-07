from flask import Flask, render_template, request, redirect, url_for
import psycopg

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "mi_base",
    "user": "postgres",
    "password": "ratonmalvado",
    "host": "localhost",
    "port": "5432"
}

@app.route('/')
def index():
    productos = []
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM productos")
                filas = cur.fetchall()
                productos = []
                for producto in filas:
                    productos.append({
                        'id': producto[0],
                        'descripcion': producto[1],
                        'categoria': producto[2],
                        'precio': producto[3],
                        'cantidad': producto[4],
                        'fecha_fabricacion': producto[5]
                    })
    except Exception as e:
        return render_template('index.html', mensaje='Error%20al%20cargar%20los%20productos:%20' + str(e), productos=productos)
    return render_template('index.html', productos=productos)

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    descripcion = request.form['descripcion']
    categoria = request.form['categoria']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    fecha_fabricacion = request.form['fecha_fabricacion']

    if descripcion and categoria and precio and cantidad and fecha_fabricacion:
        try:
            with psycopg.connect(**DB_CONFIG) as conn:
                with conn.cursor() as cur:
                    cur.execute("""INSERT INTO productos (descripcion, categoria, precio, cantidad, fecha_fabricacion) 
                                VALUES (%s, %s, %s, %s, %s)""", (descripcion, categoria, precio, cantidad, fecha_fabricacion))
                    conn.commit()
            return redirect(url_for('index', mensaje='Producto%20agregado%20con%20exito'))
        except Exception as e:
            return redirect(url_for('index', mensaje='Error%20al%20agregar%20el%20producto:%20' + str(e)))
    else:
        return redirect(url_for('index', mensaje='Todos%20los%20campos%20son%20obligatorios'))
    
@app.route('/eliminar_producto/<int:id>')
def eliminar_producto(id):
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM productos WHERE id = %s", (id,))
                conn.commit()
        return redirect(url_for('index', mensaje='Producto%20eliminado%20correctamente'))
    except Exception as e:
        return redirect(url_for('index', mensaje='Error%20al%20eliminar' + str(e)))
    
@app.route('/editar_producto/<int:id>')
def editar_producto(id):
    producto_a_editar = {}
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM productos WHERE id = %s", (id,))
                producto = cur.fetchone()
                if producto:
                    producto_a_editar = {
                        'id': producto[0],
                        'descripcion': producto[1],
                        'categoria': producto[2],
                        'precio': producto[3],
                        'cantidad': producto[4],
                        'fecha_fabricacion': producto[5]
                    }
    except Exception as e:
        return redirect(url_for('index', mensaje='Error%20al%20cargar' + str(e)))
    return render_template('editar.html', producto=producto_a_editar)

@app.route('/actualizar_producto/<int:id>', methods=['POST'])
def actualizar_producto(id):
    descripcion = request.form['descripcion']
    categoria = request.form['categoria']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    fecha_fabricacion = request.form['fecha_fabricacion']

    if descripcion and categoria and precio and cantidad and fecha_fabricacion:
        try:
            with psycopg.connect(**DB_CONFIG) as conn:
                with conn.cursor() as cur:
                    cur.execute("UPDATE productos SET descripcion=%s, categoria=%s, precio=%s, cantidad=%s, fecha_fabricacion=%s WHERE id=%s", 
                                (descripcion, categoria, precio, cantidad, fecha_fabricacion, id))
                    conn.commit()
            return redirect(url_for('index', mensaje='Producto%20actualizado%20con%20exito'))
        except Exception as e:
            return redirect(url_for('index', mensaje='Error%20al%20actualizar%20el%20producto:%20' + str(e)))
    else:
        return redirect(url_for('index', mensaje='Todos%20los%20campos%20son%20obligatorios'))
    
if __name__ == '__main__':
    app.run(debug=True, port=5000)