import pandas as pd
from datetime import datetime

class cliente:
    """
    Clase cliente que representa a un cliente del banco."""
    def __init__(self, nombre, ci):
        self.nombre = nombre
        self.ci = ci
        # Lista de cuentas asociadas al cliente
        # Cada cuenta es una instancia de la clase cuenta_corriente
        self.cuentas = []
    
    def mostrar_cuentas(self):
        # Usando join con el separador de nueva línea para mostrar las cuentas
        # Enumerate para obtener el índice y el saldo de cada cuenta, con compresión de listas
        cuentas_info = [f"Cuenta número: {idx + 1}, Saldo: {cuenta.saldo}" for idx, cuenta in enumerate(self.cuentas)]
        return "\n".join(cuentas_info)
    
    def __str__(self):
        return f"Nombre: {self.nombre}, \nCI: {self.ci}, \nCuentas:\n{self.mostrar_cuentas()}"
    
    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

class cuenta_corriente:
    """
    Clase cuenta_corriente que representa una cuenta corriente de un cliente."""
    def __init__(self, cliente, saldo=0):
        self.cliente = cliente
        self.saldo = saldo
        # Lista de diccionarios para almacenar los movimientos
        # Cada diccionario tendrá tipo, monto y fecha
        self.movimientos = []
    
    def depositar(self, monto):
        self.saldo += monto
        self.movimientos.append({"tipo": "depósito", "monto": monto, "fecha": datetime.now()})
    
    def retirar(self, monto):
        if monto > self.saldo:
            # Si el monto a retirar es mayor que el saldo, se lanza una excepción
            # ValueError es una excepción que indica que se ha pasado un argumento inválido
            raise ValueError("Fondos insuficientes")
        self.saldo -= monto
        self.movimientos.append({"tipo": "retiro", "monto": monto, "fecha": datetime.now()})
    
    def mostrar_saldo(self):
        return f"Saldo: {self.saldo}"

    def generar_extracto_excel(self, archivo_excel):
        """
        Genera un extracto de la cuenta en un archivo Excel con los movimientos realizados."""
        data = {
            #Usando la compresión de listas para crear un diccionario con los datos de los movimientos
            # "Tipo" contiene el tipo de movimiento (depósito o retiro)
            "Tipo": [mov["tipo"] for mov in self.movimientos],
            # "Monto" contiene el monto del movimiento
            "Monto": [mov["monto"] for mov in self.movimientos],
            # "Fecha" contiene la fecha del movimiento formateada como cadena
            # usando strftime para formatear la fecha
            "Fecha": [mov["fecha"].strftime("%Y-%m-%d %H:%M:%S") for mov in self.movimientos],
        }
        # Crear un DataFrame de pandas a partir del diccionario de datos
        df = pd.DataFrame(data)
        try:
            df.to_excel(archivo_excel, index=False)
            print(f"Extracto guardado en el archivo: {archivo_excel}")
        except Exception as e:
            print(f"Error al guardar el extracto: {e}")
    
    def __str__(self):
        movimientos_str = "\n".join(f"Tipo: {mov['tipo']}, Monto: {mov['monto']}, Fecha: {mov['fecha']}" for mov in self.movimientos)
        return f"Saldo: {self.saldo}\nMovimientos:\n{movimientos_str}"

# Crear instancias de cliente y cuenta
john = cliente("John Pérez", 4256987)
maria = cliente("María López", 3569847)
# Crear cuentas para los clientes
john_cuenta = cuenta_corriente(john, 3500000)
maria_cuenta = cuenta_corriente(maria, 1500000)
# Agregar cuentas a los clientes
john.agregar_cuenta(john_cuenta)
maria.agregar_cuenta(maria_cuenta)
# Realizar operaciones
john_cuenta.depositar(500000)
john_cuenta.retirar(1000000)
maria_cuenta.depositar(200000)
# Guardar extractos en archivos Excel
john_cuenta.generar_extracto_excel("extracto_john.xlsx")
maria_cuenta.generar_extracto_excel("extracto_maria.xlsx")