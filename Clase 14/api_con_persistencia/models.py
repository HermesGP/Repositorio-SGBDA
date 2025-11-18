class Usuario:
    def __init__(self, id, nombre, cedula, correo_electronico, telefono, fecha_nacimiento):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula
        self.correo_electronico = correo_electronico
        self.telefono = telefono
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f'Usuario(id={self.id}, nombre={self.nombre}, correo_electronico={self.correo_electronico}, telefono={self.telefono}, fecha_nacimiento={self.fecha_nacimiento})'
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cedula": self.cedula,
            "correo_electronico": self.correo_electronico,
            "telefono": self.telefono,
            "fecha_nacimiento": self.fecha_nacimiento
        }