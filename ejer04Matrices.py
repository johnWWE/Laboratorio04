'''4. Hallar la matriz transpuesta'''

filas      =  int(input("Ingrese la cantidad de filas de la matriz A: "))
columnas   =  int(input("Ingrese la cantidad de columnas de la matriz A: "))
print("La matriz que usted desea calcular es de orden ", filas,"*", columnas)
#creando una matriz vacia para poner los elementos introdducidos por teclado
matrizA  = []
for i in range(filas):
    matrizA.append([0]* columnas)

#llenando los elementos de la matriz
for fila in range(filas):
    for columna in range(columnas):
        matrizA[fila][columna]= int(
            input(f'Ingrese la posicion {fila+1},{columna+1}: ')
        )

#mostrando la matrizA parar luego poder comparaar visualmente con su transpuesta
print('\nMatriz A \n')
for i in matrizA:
    print(i)

 # otra matriz vacia para aalmacenar la transpuesta de la matriz original
matrizTranspuesta = []
for i in range(columnas):
     matrizTranspuesta.append([0]* filas)
#despues de recorrer el mismo orden, hacemos que la filas sean columnas y la columnas sea filas
for fila in range(columnas):
        for columna in range(filas):
            matrizTranspuesta[fila][columna] = matrizA[columna][fila]
#mostramos la transpuesta de la matriz A
print('\nMatriz Transpuesta de A \n')
for i in matrizTranspuesta:
    print(i)