'''Crea dos arrays o arreglos unidimensionales que tengan
el mismo tamaño (lo pedirá por teclado), en uno de ellos
almacenarás nombres de personas como cadenas, en el
otro array o arreglo ira almacenando la longitud de los
nombres.'''
tamanAArreglo = int(input("Ingrese el tamanio de la matriz: "))
nombres = []
datos= []
for i in range(tamanAArreglo):
    nombres.append(input("Ingrese el nombre: "))
print(nombres)    
for j in range(tamanAArreglo):
    datos.append(len(nombres[j]))
print(datos)