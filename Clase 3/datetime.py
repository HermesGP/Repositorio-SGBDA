
from datetime import datetime

# Imprimir el dia y hora actuales con datetime
print("Fecha y hora actuales: " , datetime.now())

# cargar una cierta fecha
dia = int(input("Introduzca el dia: "))
mes = int(input("Introduzca el mes: "))
año = int(input("Introduzca el año: "))

fecha = datetime(año ,mes ,dia)

# Imprime los diversos formatos de datetime del dia de hoy:
print("Año: ", fecha.strftime("%Y"))
print("Mes del año: ", fecha.strftime("%B"))
print("Numero de semana: ", fecha.strftime("%W"))
print("Número de Día de la semana: ", fecha.strftime("%w"))
print("Día del año: ", fecha.strftime("%j"))
print("Día de la semana: ", fecha.strftime("%A")) 

