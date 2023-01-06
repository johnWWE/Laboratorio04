'''matriz simetrica'''
#s dice simetrica donde su matriz traspuesta es igual a la matriz original.
filasA      =  int(input("Ingrese la cantidad de filas de la matriz A: "))
columnasA  =  int(input("Ingrese la cantidad de columnas de la matriz A: "))
contador = 0
#necesaariamente tiene que ser una matriz cuadrada
if columnasA == filasA:

    # Creando la matriz vacía
    matrizA = []
    for i in range(filasA):
        matrizA.append([0] * columnasA)

    # Rellenando la matriz
    print('Ingrese la matriz A')
    for fila in range(filasA):
        for columna in range(columnasA):
            matrizA[fila][columna] = float(
                input("Introduce el elemento ["+str(fila+1)+","+str(columna+1)+"] de la matriz:"))

    # Calculando si una matriz es simétrico o no lo es, para ello su transpuesta tiene que ser igual a la original
    for fila in range(filasA):
        for columna in range(columnasA):
            normal = matrizA[fila][columna]
            transpuesta = matrizA[columna][fila]
            if normal == transpuesta:
                contador += 1

#imprimir los resultados
    if contador == (filasA * columnasA):
        print('La matriz introducida es simétrica')
    else:
        print('La matriz introducida NO es simétrica')
else:
    print('La matriz  introducida no es simétrica')