'''Crea un array o arreglo unidimensional donde le indiques
el tamaño por teclado y crear una función que rellene
el array o arreglo con los múltiplos de un número pedido
por teclado.
Por ejemplo, si defino un array de tamaño 5 y elijo un
3 en la función, el array contendrá 3, 6, 9, 12, 15.
Muéstralos por pantalla usando otra función distinta.'''    
#definimos los arrays 
'''tamanArreglo = int(input("Ingrese el tamaño del arreglo : "))
multiplo     = int(input("Ingrese el número de múltiplos : "))
#creando una lista vacia para almacenar los valores dentro de ella
A = []
# par que obvie el cero y que vaye hasta el numero indicado
for i in range (1,tamanArreglo+1):      
    A.append(i*multiplo)
print(A)'''

tamanArreglo = int(input("Ingrese el tamaño del arreglo : "))
#definiendo una funcion
def rellenar():
    multiplo     = int(input("Ingrese el número de múltiplos : "))
    A=[]
    for i in range (1,tamanArreglo+1):      
        A.append(i*multiplo)
    print(A)
rellenar()


