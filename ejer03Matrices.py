'''3. Calcular la diagonal principal de una matriz'''

filas      =  int(input("Ingrese la cantidad de filas de la matriz A: "))
columnas  =  int(input("Ingrese la cantidad de columnas de la matriz A: "))

#en la variable diagonal almacenaremos los valores de las diagonales para sumarlas
diagonal = 0

if filas == columnas:    #matriz cuadrada

    # Creando la matriz vacía
    matrizA = []
    for i in range(filas):
        matrizA.append([0] * columnas)

    # Rellenando la matriz
    #print('Ingrese la matriz A')
    for fila in range(filas):
        for columna in range(columnas):              
            matrizA[fila][columna] = float(
                input("Introduce el elemento ["+str(fila+1)+","+str(columna+1)+"] de la matriz:"))

    # Calculando la diagonal principal de la matriz A
    for fila in range(filas):
        for columna in range(columnas):
            if fila == columna:
                diagonal += matrizA[fila][columna]
    
    print(f'El valor de la diagonal principal es: {diagonal}')