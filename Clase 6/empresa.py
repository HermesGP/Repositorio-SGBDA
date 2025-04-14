class persona:
    def __init__(self, id, nombre, email):
        self.__id = id
        self.__nombre = nombre
        self.__email = email
    
    def get_id(self):
        return self.__id
    
    def get_nombre(self):
        return self.__nombre
    
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
    
    def __str__(self):
        return f"ID: {self.__id}, Nombre: {self.__nombre}, Email: {self.__email}"

class cliente(persona):
    def __init__(self, id, nombre, email, ruc):
        super().__init__(id, nombre, email)
        self.__ruc = ruc
        self.__historial_compras = []
    
    def agregar_compra(self, compra):
        self.__historial_compras.append(compra)
    
    def mostrar_historial(self):
        return "\n".join(str(compra) for compra in self.__historial_compras)
    
    def get_ruc(self):
        return self.__ruc
    
    def __str__(self):
        compras_str = self.mostrar_historial() if self.__historial_compras else "Sin compras"
        return f"{super().__str__()}, RUC: {self.__ruc}, Compras: {compras_str}"

class compra:
    def __init__(self, id, monto, fecha):
        self.__id = id
        self.__monto = monto
        self.__fecha = fecha
    
    def __str__(self):
        return f"ID: {self.__id}, Monto: {self.__monto}, Fecha: {self.__fecha}"

class empleado(persona):
    def __init__(self, id, nombre, email, cargo, salario_base):
        super().__init__(id, nombre, email)
        self.__cargo = cargo
        self.__salario_base = salario_base
    
    def get_cargo(self):
        return self.__cargo
    
    def get_salario_base(self):
        return self.__salario_base
    
    def __str__(self):
        return f"{super().__str__()}, Cargo: {self.__cargo}, Salario Base: {self.__salario_base}"