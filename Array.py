import numpy as np
lista=[1,2,3,4,5,6]

arr = np.array(lista)

print(arr)


matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])

print(matriz)


#mostrando apartir de indexado 

print(arr[0])

print(matriz[0,1])

#usando slices para acceder los primreos 3 valore o lso que queramos
print(arr[0:3])

print("imprimeindo la matriz con slices" ,matriz[0:2,0:2])

