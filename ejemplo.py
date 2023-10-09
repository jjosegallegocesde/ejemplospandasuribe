import pandas as pd

#################################################################
#lista sola
# Lista de ciudades
ciudades = ['Madrid', 'Barcelona', 'Sevilla', 'Valencia']
# Crear un DataFrame con una sola columna 'Ciudad'
df = pd.DataFrame({'Ciudad': ciudades})
#################################################################
# Lista de diccionarios datos
data = [
    {'Nombre': 'Juan', 'Edad': 25, 'Ciudad': 'Madrid'},
    {'Nombre': 'Ana', 'Edad': 30, 'Ciudad': 'Barcelona'},
    {'Nombre': 'Carlos', 'Edad': 22, 'Ciudad': 'Sevilla'},
    {'Nombre': 'Laura', 'Edad': 28, 'Ciudad': 'Valencia'},
]
df2 = pd.DataFrame(data, columns=['Ciudad'])
#################################################################
# Diccionario con los datos
datos = {'Nombre': 'Juan', 'Edad': 25, 'Ciudad': 'Madrid'}
df3 = pd.DataFrame([datos])
#################################################################
# Datos ficticios para 50 empleados
df4 = pd.read_csv('./empleados.csv',encoding='utf-8')
