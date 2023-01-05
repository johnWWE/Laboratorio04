''' Multiplicación de matrices.'''
import numpy
import sys

filaA    = int(input("Introduce el numero de filas para la matriz A: "))
columnaA = int(input("Introduce el numero de columnas para la matriz A: "))
filaB    = int(input("Introduce el numero de filas para la matriz B: "))
columnaB = int(input("Introduce el numero de columnas para la matriz B: "))
#antes de la operacion, debemos verificar si las matrices se pueden multiplicar
if (columnaA != filaB):
    print("Las matrices de las ordenes introducidas no se puede multiplicar")
    sys.exit()   # si al condicional no se cumple, auotmticament teremina el programa

matrizA   =  numpy.zeros((filaA,columnaA))   #convertimos en forma ded amtriz, algebraicamente
matrizB   = numpy.zeros((filaB,columnaB))
matrizResultado =numpy.zeros((filaA,columnaB))
# llenado de los elementos de ambas matrices
print("introduce los elementos de la matriz A ")
for i in range(0,filaA):                #recorremos la cantidad de veces del tamanio de su fila de la matriz A
    for j in range(0,columnaA):         # igual forma para el tamnio de su columna
        matrizA[i,j]=int(input("Elemento ["+str(i+1)+","+str(j+1)+"] de A:"))     #empezamos a almacenar los elementos en cada posicion 
print("introduce los elementos de la matriz B")
for i in range(0,filaB):
    for j in range(0,columnaB):
        matrizB[i,j]=int(input("Elemento [" + str(i+1)+","+str(j+1)+"] de B:"))
#operando
print("/............................................/")
print("El resultado de la matriz  A * B es:")
for i in range (0, filaA):
    for j in range(0,columnaB):
        for k in range(0,filaB):
            matrizResultado[i,j]+= matrizA[i,k] * matrizB[k,j]
print(matrizResultado)
