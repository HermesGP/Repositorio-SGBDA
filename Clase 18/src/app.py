from flask import Flask, render_template, request, redirect
import psycopg

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/agregar_producto', methods=['POST'])
def agregar_producto():
    descripcion = request.form['descripcion']
    categoria = request.form['categoria']
    precio = request.form['precio']
    cantidad = request.form['cantidad']
    fecha_fabricacion = request.form['fecha_fabricacion']

    if descripcion and categoria and precio and cantidad and fecha_fabricacion:
        try:
            with psycopg.connect(                
                dbname='mi_base',
                user='postgres',
                password='ratonmalvado',
                host='localhost',
                port='5432'
            ) as conn:
                with conn.cursor() as cur:
                    cur.execute("""INSERT INTO productos (descripcion, categoria, precio, cantidad, fecha_fabricacion) 
                                VALUES (%s, %s, %s, %s, %s)""", (descripcion, categoria, precio, cantidad, fecha_fabricacion))
                    conn.commit()
            return redirect('/?mensaje=Producto%20agregado%20con%20exito')
        except Exception as e:
            return redirect(f'/?mensaje=Error%20al%20agregar%20el%20producto:%20{str(e)}')
    else:
        return redirect('/?mensaje=Todos%20los%20campos%20son%20obligatorios')

if __name__ == '__main__':
    app.run(debug=True, port=5000)