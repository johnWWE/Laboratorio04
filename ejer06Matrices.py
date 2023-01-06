'''Hallando la determinando de una matriz'''
import numpy as np

filas    = int(input("Introduce el numero de filas de la matriz : "))
columnas = int(input("Introduce el numero de columnas de la matriz : "))

# creamos una matriz nula para llenar los elemntos en ella
matriz =[]
for i in range (filas):
    matriz.append([0] *columnas)  #se iran guardando todos  en orden 

# empezaremos con el proceso del llenado de la matriz por consola
for fila in range(filas):
    for columna in range(columnas):
        matriz[fila][columna]=int(
        input("Introduce el elemento ["+str(fila+1)+","+str(columna+1)+"] de la matriz=> "))

#este mtdo del np.linalg es un afuncion especializada para realizar calculo de algebra lineal
#en este caso lo estamos usando para resolver la determinante de un amatriz cuadrada
determinante =  np.linalg.det(matriz)
print(determinante)