import tkinter as tk

def saludar():
    nombre = entry_nombre.get()
    label2.configure(text= f"Hola, {nombre}")

ventana1 = tk.Tk()
ventana1.title("Programa para saludar")

ventana1.columnconfigure(0,minsize=300, weight=1)
ventana1.rowconfigure([1,2,3,4], minsize=50, weight=1)

label1 = tk.Label(ventana1, text= "Ingrese su nombre: ")
label1.grid(column=0,row=1)

entry_nombre = tk.Entry(ventana1, width=20)
entry_nombre.grid(column=0, row=2)

btn_leer = tk.Button(ventana1, width=15, text="Saludame", command = saludar)
btn_leer.grid(column=0, row=3)

label2 = tk.Label(ventana1, text="")
label2.grid(column=0, row=4)

ventana1.mainloop()