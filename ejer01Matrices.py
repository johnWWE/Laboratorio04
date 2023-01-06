''' 1. Suma, resta, multiplicación de matrices.'''
import numpy

#introduciomos el orden para la matriz A y la Matriz B respectivamente
filaA    = int(input("Introduce el numero de filas para la matriz A: "))
columnaA = int(input("Introduce el numero de columnas para la matriz A: "))
print("...El orden de la matriz A es: ", filaA, "*",columnaA,".....")
filaB   = int(input("Introduce el numero de filas para la matriz B: "))
columnaB = int(input("Introduce el numero de columnas para la matriz B: "))
print("...El orden de la matriz B es: ", filaB, "*",columnaB,".....")
#creamos la matriz A,B y la matriz resultante en la que almacenaremos la suma de nuestras matrices
matrizA   =  numpy.zeros((filaA,columnaA))
matrizB   = numpy.zeros((filaB,columnaB))
matrizResult =numpy.zeros((filaA,columnaA))
#para poder sumar dos matrices,es necesario que el orden sea exacto 
if filaA == filaB and columnaA ==columnaB:
    #matrizA
    for i in range(0,filaA):
        for j in range(0,columnaA):
            matrizA[i][j]=int(input("Introduce el Elemento A["+str(i+1)+","+str(j+1)+"] =>"))
    print(f"matriz A: \n{matrizA}")
    #matrizB
    for i in range(0,filaA):
        for j in range(0,columnaA):
            matrizB[i][j]=int(input("Introduce el Elemento B["+str(i+1)+","+str(j+1)+"]=>"))
    print(f"matriz B: \n{matrizB}")
#operacion
    for i in range(0,filaA):
        for j in range(0,columnaA):
            #for k in range(0,filaA):
            matrizResult[i][j] = matrizA[i][j] + matrizB[i][j]
    print(f".....matriz resultado A + B.....: \n{matrizResult}")
else:
    print("las Matrices A y B no se pueden sumar")

#producto
''' Evidentemente para el producto de matrices existen ciertas condiciones mas especificas
que en una suma o resta de matrices'''
