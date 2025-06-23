import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de Tkinter con Grid")

tk.Label(root, text="Nombre del club:").grid(row=0, column=0, padx=10, pady=5)
entry_nombre = tk.Entry(root)
entry_nombre.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

tk.Label(root, text="Pais:").grid(row=1, column=0, padx=10, pady=5)
entry_edad = tk.Entry(root)
entry_edad.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

# Función para mostrar los datos en un MessageBox
def mostrar_datos():
    nombre = entry_nombre.get()
    pais = entry_edad.get()
    messagebox.showinfo("Datos Ingresados", f"Club de futbol: {nombre}\nEs del pais: {pais}")

# Botón para mostrar los datos
btn_mostrar = tk.Button(root, text="Mostrar Datos", command=mostrar_datos)
btn_mostrar.grid(row=2, column=0, columnspan=2, pady=10)

# Ejecutar la aplicación
root.mainloop()