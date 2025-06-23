#Ejemplo de programa de tkinter encapsulado con clases
import tkinter as tk

class Aplicacion:
    def __init__(self):
        #iniciando la ventana
        self.ventana1 = tk.Tk()
        self.ventana1.title("Saluditos")

        #configuracion del grid
        self.ventana1.columnconfigure(0,minsize=250, weight=1)
        self.ventana1.rowconfigure([1,2,3,4],minsize=50, weight=1)

        self.label1=tk.Label(self.ventana1, text = "Ingrese su nombre")
        self.label1.grid(column=0, row=1)

        self.entry_nombre=tk.Entry(self.ventana1, width=30)
        self.entry_nombre.grid(column=0, row=2)

        self.boton1=tk.Button(self.ventana1, width=25, text="Salúdame", command=self.saludar)
        self.boton1.grid(column=0,row=3)

        self.label2=tk.Label(self.ventana1, text="")
        self.label2.grid(column=0, row=4)
        
        self.ventana1.mainloop()
    
    def saludar(self):
        texto = self.entry_nombre.get()
        self.label2.configure(text= "Hola " + texto)

if __name__ == "__main__":
    aplicacion1 = Aplicacion()