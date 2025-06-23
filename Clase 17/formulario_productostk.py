import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import psycopg
import datetime
from decimal import Decimal

def limpiar_formulario():
    entry_descripcion.delete(0, tk.END)
    entry_categoria.delete(0, tk.END)
    spin_precio.delete(0, tk.END)
    spin_precio.insert(0, "500")
    spin_cantidad.delete(0,tk.END)
    spin_cantidad.insert(0, "1")
    date_picker.set_date(datetime.date.today())

def guardar_producto():
    descripcion= entry_descripcion.get()
    categoria = entry_categoria.get()
    precio = spin_precio.get()
    cantidad = spin_cantidad.get()
    fecha_fabricacion = date_picker.get_date()

    if not descripcion or not categoria or not precio or not cantidad:
        messagebox.showwarning("Advertencia", "Faltaron campos obligatorios")
        return
    try:
        precio = Decimal(precio)
        cantidad = Decimal(cantidad)
    except ValueError:
        messagebox.showerror("Error", "No se cargaron números válidos")

    try:
        with psycopg.connect(
            dbname='mi_base',
            user='postgres',
            password='ratonmalvado',
            host='localhost',
            port='5432'
        ) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO productos (descripcion, categoria, precio, cantidad, fecha_fabricacion) VALUES (%s, %s, %s, %s, %s)",
                    (descripcion, categoria, precio, cantidad, fecha_fabricacion))
                conn.commit()
        messagebox.showinfo("Éxito", "Producto guardado satisfactoriamente")
        limpiar_formulario()
    except Exception as e:
        messagebox.showerror("Error de base de datos", e)

root = tk.Tk()
root.title("Registro de productos")

root.grid_rowconfigure([0,1,2,3,4,5], weight=1)
root.grid_columnconfigure([0 , 1], weight=1)

tk.Label(root, text="Descripción: ", font=("Calibri", 11)).grid(row=0, column=0, padx=5, pady=5)
entry_descripcion = tk.Entry(root)
entry_descripcion.grid(row=0, column=1, padx=15, pady=5 , sticky="ew")

tk.Label(root, text="Categoria: ", font=("Calibri", 11)).grid(row=1, column=0, padx=5, pady=5)
entry_categoria = tk.Entry(root)
entry_categoria.grid(row=1, column=1, padx=15, pady=5 , sticky="ew")

tk.Label(root, text="Precio: ", font=("Calibri", 11)).grid(row=2, column=0, padx=5, pady=5)
spin_precio = tk.Spinbox(root, from_=500, to=3000000, increment=500)
spin_precio.grid(row=2, column=1, padx=15, pady=5 , sticky="ew")

tk.Label(root, text="Cantidad: ", font=("Calibri", 11)).grid(row=3, column=0, padx=5, pady=5)
spin_cantidad = tk.Spinbox(root, from_=1, to=10000, increment=1)
spin_cantidad.grid(row=3, column=1, padx=15, pady=5 , sticky="ew")

tk.Label(root, text="Fecha de fabricación: ", font=("Calibri", 11)).grid(row=4, column=0, padx=5, pady=5)
date_picker = DateEntry(root)
date_picker.grid(row=4, column=1, padx=15, pady=5 , sticky="ew")

btn_guardar = tk.Button(root, text="Guardar", command=guardar_producto)
btn_guardar.grid(row=5, column=1, pady=15, padx=15, sticky="ew")

btn_guardar = tk.Button(root, text="Limpiar", command=limpiar_formulario)
btn_guardar.grid(row=5, column=0, pady=15, padx=15, sticky="ew")

root.mainloop()

