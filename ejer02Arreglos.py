'''Dada las siguientes notas almacenadas en un arreglo:
[20, 15, 12, 11, 8, 4, 1]
Elimine la nota más baja programáticamente sin usar la
función (min) y escriba en pantalla.
Luego programáticamente calcule el promedio de notas
descontando la nota eliminada.'''

notas = [20, 15, 12, 11, 8, 4, 1]      #creamos una lista de notas
notaMaxima = 20          
notaMinima = notaMaxima      # en ella lo ponemos como nota maxima para que almacene el valor mas pequenio
for i in notas:        #recorremos los valores de las notas
    if i<notaMinima:      # comparamos si el iterador(valores de las notas) es menor  que  la nota maxima
        notaMinima= i      # y si lo fuera dentro de la nota minima lo guaardamos ese valor
notas.remove(notaMinima)         #borramos la nota minima
print("Las nuevas notas quedan de la sgt. forma " ,notas)    #se imprime las nuevas notas
suma= 0         #creamos una variable para aalamcenar la suma
for j in notas:    # recorremos los nuevos valores de nota
    suma = suma +j    # y dentro de suma vamos sumando todos los valores de notas
print("El promedio de las notas es",round(suma/len(notas),2))    # el promedio es la suma de las notas entre la cantidad de vaalores en ella
                                                                # mostramos con solo dos decimales