import tkinter as tk

class Aplicacion:
    def sumar_1(self):
        self.valor =  self.valor + 1
        self.label_valor.config(text=self.valor)
    
    def restar_1(self):
        self.valor = self.valor - 1
        self.label_valor.config(text= self.valor)

    def __init__(self):
        self.valor = 0

        self.root = tk.Tk()
        self.root.title("Contador")

        self.root.columnconfigure(0, minsize=200, weight=1)
        self.root.rowconfigure([0,1,2], minsize=50, weight=1)

        self.label_valor = tk.Label(self.root, text=self.valor, font=("Calibri", 30))
        self.label_valor.grid(column=0,row=0)

        self.boton_sumar = tk.Button(self.root, text="Sumar 1", width=50,height=2, command=self.sumar_1)
        self.boton_sumar.grid(column=0, row=1, padx=30)

        self.boton_restar = tk.Button(self.root, text="Restar 1", width=50,height=2,command=self.restar_1)
        self.boton_restar.grid(column=0,row=2, padx=30)

        self.root.mainloop()

if __name__ == "__main__":
    aplicacion1 = Aplicacion()
