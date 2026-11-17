import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import psycopg
import datetime
from decimal import Decimal
def conectar_bd():
    return psycopg.connect(
        dbname="mi_base",
        user="postgres",
        password="@lumno123",
        host="localhost",
        port="5432"
    )

def actualizar_lista():
    listbox.delete(0, tk.END)
    try:
            with conectar_bd() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT id, descripcion, categoria, precio , cantidad, fecha_compra FROM productos")
                    for fila in cur.fetchall():
                        listbox.insert(tk.END, f"{fila[0]} | {fila[1]} | {fila[2]} | {fila[3]:.2f} | {fila[4]:.2f} | {fila[5]}")
    except Exception as e:
        messagebox.showerror("Error en la carga de productos: ", str(e))

def editar_producto():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Favor seleccionar un producto")
        return
    datos = listbox.get(seleccion[0]).split(" | ")
    id_producto = datos[0]

    def limpiar_formulario():
        entry_descripcion.delete(0,tk.END)
        entry_categoria.delete(0,tk.END)
        spin_precio.delete(0,tk.END)
        spin_precio.insert(0, "500")
        spin_cantidad.delete(0,tk.END)
        spin_cantidad.insert(0, "1")
        date_picker.set_date(datetime.date.today())

    def guardar_producto():
        descripcion = entry_descripcion.get()
        categoria = entry_categoria.get()
        precio = spin_precio.get()
        cantidad = spin_cantidad.get()
        fecha_compra = date_picker.get_date()

        if not descripcion or not categoria or not precio or not cantidad:
            messagebox.showwarning("Advertencia", "Faltan campos obligatorios")
            return
        try:
            precio = Decimal(precio)
            cantidad = Decimal(cantidad)
        except ValueError:
            messagebox.showerror("Error", "No se cargaron números correctos")
            return

        try:
            with conectar_bd() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "UPDATE productos SET descripcion =%s , categoria=%s, precio=%s,  cantidad=%s, fecha_compra=%s WHERE id=%s",
                        (descripcion,categoria,precio,cantidad, fecha_compra, id_producto)
                    )
                    conn.commit()
                    nuevo.destroy()
                    actualizar_lista()
                    messagebox.showinfo("Éxito", f"Producto {descripcion} actualizado correctamente.")
        except Exception as e:
            messagebox.showerror("Error de base de datos", str(e))

    nuevo = tk.Toplevel(root)
    nuevo.title("Editar Producto")
    nuevo.rowconfigure([0,1,2,3,4,5], weight=1)
    nuevo.columnconfigure([0 , 1],weight=1)

    tk.Label(nuevo, text="Descripción: ").grid(row=0,column=0,padx=5,pady=5)
    entry_descripcion = tk.Entry(nuevo)
    entry_descripcion.grid(row=0,column=1, padx=15, pady=5, sticky="ew")
    entry_descripcion.insert(0, datos[1])

    tk.Label(nuevo, text="Categoria: ").grid(row=1,column=0,padx=5,pady=5)
    entry_categoria = tk.Entry(nuevo)
    entry_categoria.grid(row=1,column=1, padx=15, pady=5, sticky="ew")
    entry_categoria.insert(0, datos[2])

    tk.Label(nuevo, text="Precio: ").grid(row=2,column=0,padx=5,pady=5)
    spin_precio = tk.Spinbox(nuevo,from_=500, to=5000000, increment=100)
    spin_precio.grid(row=2,column=1, padx=15, pady=5, sticky="ew")
    spin_precio.insert(0, datos[3])

    tk.Label(nuevo, text="Cantidad: ").grid(row=3,column=0,padx=5,pady=5)
    spin_cantidad = tk.Spinbox(nuevo,from_=1, to=10000, increment=1)
    spin_cantidad.grid(row=3,column=1, padx=15, pady=5, sticky="ew")
    spin_cantidad.insert(0, datos[4])

    tk.Label(nuevo, text="Fecha de compra: ").grid(row=4,column=0,padx=5,pady=5)
    date_picker = DateEntry(nuevo, date_pattern='yyyy-mm-dd')
    date_picker.grid(row=4,column=1, padx=15, pady=5, sticky="ew")
    date_picker.set_date(datos[5])

    btn_guardar = tk.Button(nuevo, text="Guardar", command=guardar_producto)
    btn_guardar.grid(row=5,column=1,padx=15,pady=15, sticky="ew")

    btn_limpiar = tk.Button(nuevo, text="Limpiar", command=limpiar_formulario)
    btn_limpiar.grid(row=5, column=0, padx=15, pady=15, sticky="ew")

def borrar_producto():
    seleccion = listbox.curselection()
    if not seleccion:
        messagebox.showwarning("Advertencia", "Favor seleccionar un producto")
        return
    datos = listbox.get(seleccion[0]).split(" | ")
    id_producto = datos[0]
    try:
        with conectar_bd() as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM productos WHERE id=%s",(id_producto,))
                conn.commit()
            actualizar_lista()
            messagebox.showinfo("Éxito", "Producto eliminado correctamente")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")

def nuevo_producto():
    def limpiar_formulario():
        entry_descripcion.delete(0,tk.END)
        entry_categoria.delete(0,tk.END)
        spin_precio.delete(0,tk.END)
        spin_precio.insert(0, "500")
        spin_cantidad.delete(0,tk.END)
        spin_cantidad.insert(0, "1")
        date_picker.set_date(datetime.date.today())

    def guardar_producto():
        descripcion = entry_descripcion.get()
        categoria = entry_categoria.get()
        precio = spin_precio.get()
        cantidad = spin_cantidad.get()
        fecha_compra = date_picker.get_date()

        if not descripcion or not categoria or not precio or not cantidad:
            messagebox.showwarning("Advertencia", "Faltan campos obligatorios")
            return
        try:
            precio = Decimal(precio)
            cantidad = Decimal(cantidad)
        except ValueError:
            messagebox.showerror("Error", "No se cargaron números correctos")

        try:
            with conectar_bd() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        "INSERT INTO productos (descripcion, categoria, precio,  cantidad, fecha_compra) VALUES (%s,%s,%s,%s,%s)",
                        (descripcion,categoria,precio,cantidad, fecha_compra)
                    )
                    conn.commit()
                    nuevo.destroy()
                    actualizar_lista()
                    messagebox.showinfo("Éxito", f"Producto {descripcion} guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error de base de datos", str(e))

    nuevo = tk.Toplevel(root)
    nuevo.title("Nuevo Producto")
    nuevo.rowconfigure([0,1,2,3,4,5], weight=1)
    nuevo.columnconfigure([0 , 1],weight=1)

    tk.Label(nuevo, text="Descripción: ").grid(row=0,column=0,padx=5,pady=5)
    entry_descripcion = tk.Entry(nuevo)
    entry_descripcion.grid(row=0,column=1, padx=15, pady=5, sticky="ew")

    tk.Label(nuevo, text="Categoria: ").grid(row=1,column=0,padx=5,pady=5)
    entry_categoria = tk.Entry(nuevo)
    entry_categoria.grid(row=1,column=1, padx=15, pady=5, sticky="ew")

    tk.Label(nuevo, text="Precio: ").grid(row=2,column=0,padx=5,pady=5)
    spin_precio = tk.Spinbox(nuevo,from_=500, to=5000000, increment=100)
    spin_precio.grid(row=2,column=1, padx=15, pady=5, sticky="ew")

    tk.Label(nuevo, text="Cantidad: ").grid(row=3,column=0,padx=5,pady=5)
    spin_cantidad = tk.Spinbox(nuevo,from_=1, to=10000, increment=1)
    spin_cantidad.grid(row=3,column=1, padx=15, pady=5, sticky="ew")

    tk.Label(nuevo, text="Fecha de compra: ").grid(row=4,column=0,padx=5,pady=5)
    date_picker = DateEntry(nuevo)
    date_picker.grid(row=4,column=1, padx=15, pady=5, sticky="ew")

    btn_guardar = tk.Button(nuevo, text="Guardar", command=guardar_producto)
    btn_guardar.grid(row=5,column=1,padx=15,pady=15, sticky="ew")

    btn_limpiar = tk.Button(nuevo, text="Limpiar", command=limpiar_formulario)
    btn_limpiar.grid(row=5, column=0, padx=15, pady=15, sticky="ew")

root = tk.Tk()
root.title("Gestión de productos")

listbox = tk.Listbox(root, width=60,height=10)
listbox.pack(padx=10,pady=10)

frame_botones = tk.Frame(root)
frame_botones.pack()

tk.Button(frame_botones, text="Nuevo", command=nuevo_producto).grid(row=1,column=0,padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Editar", command=editar_producto).grid(row=1,column=1,padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Actualizar", command=actualizar_lista).grid(row=0,column=0,padx=5, pady=5, sticky="ew")
tk.Button(frame_botones, text="Eliminar", command=borrar_producto).grid(row=0,column=1,padx=5, pady=5, sticky="ew")

actualizar_lista()
root.mainloop()