import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from decimal import Decimal
import psycopg
import datetime

# Configuración de la base de datos
DB_CONFIG = {
    "dbname": "mi_base",
    "user": "postgres",
    "password": "ratonmalvado",
    "host": "localhost",
    "port": "5432"
}

#funciones del programa
def cargar_productos():
    for fila in tree.get_children():
        tree.delete(fila)
    try:
        with psycopg.connect(**DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM productos")
                for producto in cur.fetchall():
                    tree.insert("", "end", values=producto)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los productos: {e}")

def eliminar_producto():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Atención", "Favor elegir un producto para eliminar")
    else:
        respuesta = messagebox.askyesno("Confirmación", "¿Está seguro de eliminar el producto seleccionado?")
        if respuesta:
            id_producto = tree.item(seleccion[0], "values")[0]
            try:
                with psycopg.connect(**DB_CONFIG) as conn:
                    with conn.cursor() as cur:
                        cur.execute("DELETE FROM productos WHERE id = %s", (id_producto,))
                        conn.commit()
                cargar_productos()
                messagebox.showinfo("Éxito", "Producto eliminado")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo eliminar el producto: {e}")

def abrir_formulario(modo, producto=None):
    def guardar_producto():
        descripcion = entry_descripcion.get()
        categoria = entry_categoria.get()
        precio = spin_precio.get()
        cantidad = spin_cantidad.get()
        fecha_fabricacion = date_picker.get_date()

        try:
            precio = Decimal(precio)
            cantidad = Decimal(cantidad)
        except ValueError:
            messagebox.showerror("Error", "No se cargaron números válidos")

        try:
            with psycopg.connect(**DB_CONFIG) as conn:
                with conn.cursor() as cur:
                    if modo == "nuevo":
                        cur.execute("INSERT INTO productos (descripcion, categoria, precio, cantidad, fecha_fabricacion) VALUES (%s, %s, %s, %s, %s)",
                        (descripcion, categoria, precio, cantidad, fecha_fabricacion))
                    elif modo == "editar" and producto:
                        cur.execute("UPDATE productos SET descripcion = %s, categoria = %s, precio = %s, cantidad = %s, fecha_fabricacion = %s WHERE id = %s",
                        (descripcion, categoria, precio, cantidad, fecha_fabricacion, producto[0]))
                    conn.commit()
            ventana_formulario.destroy()
            cargar_productos()
            messagebox.showinfo("Éxito", "Producto guardado")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar los datos: {e}")
    
    #Crear ventana de formulario
    ventana_formulario = tk.Toplevel(root)
    ventana_formulario.title("Nuevo Producto" if modo == "nuevo" else "Editar Producto")

    tk.Label(ventana_formulario, text="Descripción: ", font=("Calibri", 11)).grid(row=0, column=0, padx=5, pady=5)
    entry_descripcion = tk.Entry(ventana_formulario)
    entry_descripcion.grid(row=0, column=1, padx=15, pady=5 , sticky="ew")

    tk.Label(ventana_formulario, text="Categoria: ", font=("Calibri", 11)).grid(row=1, column=0, padx=5, pady=5)
    entry_categoria = tk.Entry(ventana_formulario)
    entry_categoria.grid(row=1, column=1, padx=15, pady=5 , sticky="ew")

    tk.Label(ventana_formulario, text="Precio: ", font=("Calibri", 11)).grid(row=2, column=0, padx=5, pady=5)
    spin_precio = tk.Spinbox(ventana_formulario, from_=500, to=3000000, increment=500)
    spin_precio.grid(row=2, column=1, padx=15, pady=5 , sticky="ew")

    tk.Label(ventana_formulario, text="Cantidad: ", font=("Calibri", 11)).grid(row=3, column=0, padx=5, pady=5)
    spin_cantidad = tk.Spinbox(ventana_formulario, from_=1, to=10000, increment=1)
    spin_cantidad.grid(row=3, column=1, padx=15, pady=5 , sticky="ew")

    tk.Label(ventana_formulario, text="Fecha de fabricación: ", font=("Calibri", 11)).grid(row=4, column=0, padx=5, pady=5)
    date_picker = DateEntry(ventana_formulario)
    date_picker.grid(row=4, column=1, padx=15, pady=5 , sticky="ew")

    if modo == "editar" and producto:
        entry_descripcion.insert(0, producto[1])
        entry_categoria.insert(0, producto[2])
        spin_precio.delete(0, tk.END)
        spin_precio.insert(0, producto[3])
        spin_cantidad.delete(0, tk.END)
        spin_cantidad.insert(0, producto[4])
        date_picker.set_date(datetime.datetime.strptime(producto[5], "%Y-%m-%d").date())
    
    tk.Button(ventana_formulario, text="Guardar", command=guardar_producto).grid(row=5, column=0, columnspan=2, padx=20, pady=15, sticky="ew")

def editar_producto():
    seleccion = tree.selection()
    if not seleccion:
        messagebox.showwarning("Atención", "Favor elegir un producto para editar")
    valores = tree.item(seleccion[0], "values")
    if valores:
        abrir_formulario("editar", valores)


def nuevo_producto():
    abrir_formulario("nuevo")

#Interfaz inicial
root = tk.Tk()
root.title("Registro de productos")

columnas = ("ID", "Descripción", "Categoría", "Precio", "Cantidad", "Fabricación")
tree = ttk.Treeview(root, columns=columnas, show="headings")

for col in columnas:
    tree.heading(col, text=col)
    tree.column(col, anchor="center", stretch=True, width=150 if col != "Descripción" else 250)

tree.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

#Frame de botones
botones_frame = tk.Frame(root)
botones_frame.pack(pady=15)

tk.Button(botones_frame, text="Eliminar", command=eliminar_producto).grid(row=0, column=0, padx=5)
tk.Button(botones_frame, text="Modificar", command=editar_producto).grid(row=0, column=1, padx=5)
tk.Button(botones_frame, text="Nuevo", command=nuevo_producto).grid(row=0, column=2, padx=5)

if __name__ == "__main__":
    cargar_productos()
    root.mainloop()