'''Diseñe un programa que lea un vector y calcule si hay
un número que sea igual a la suma de los demás elementos
del vector.'''

import numpy as np

vector = np.array([3,8,5,16])
print(vector[1])
if vector[3]== vector[0] +vector[1] +vector[2]:
    print('LA SUMA' )
elif vector[2] == vector[0] +vector[1]+vector[3]:
        print('LA SUMA' )
elif vector[1]== vector[0]+vector[2]+vector[3]:
        print('LA SUMA' )
elif vector[0] == vector[1]+vector[2]+vector[3]:
        print('LA SUMA' )
else:
    print("No hay un numero que sea igual a la suma de los demas elementos ")
