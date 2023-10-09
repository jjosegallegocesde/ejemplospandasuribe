import csv
import random

empleados = []
for _ in range(50):
    nombre = f'Empleado{_ + 1}'
    cargo = random.choice(['Gerente', 'Desarrollador', 'Diseñador', 'Analista'])
    edad = random.randint(22, 60)
    salario = random.randint(30000, 90000)
    ciudad = random.choice(['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao'])
    
    empleado = [nombre, cargo, edad, salario, ciudad]
    empleados.append(empleado)

# Escribir los datos en un archivo CSV con codificación UTF-8
with open('empleados.csv', mode='w', newline='', encoding='utf-8') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Nombre', 'Cargo', 'Edad', 'Salario', 'Ciudad'])  # Escribir encabezados
    writer.writerows(empleados)  # Escribir datos de empleados
