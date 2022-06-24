import numpy as np

#definiendo un escalar
escalar=np.array(42)
print(escalar, "daddo las dimensiones " , escalar.ndim)

#definiendo un vector el ucal tiene dimension 1

vector=np.array([1,2,3])
print(vector , "dando la dimension" , vector.ndim)

#creando una matriz
matriz=np.array([[1,2,3],[4,5,6],[6,7,8]])
print(matriz,"dimension de la mariz" , matriz.ndim)

#creando un tenser de 3D

tensor3d=np.array([[[1,2,3],[3,4,5],[6,7,8]],[[1,2,3],[3,4,5],[6,7,8]]])
print(tensor3d,"dando la dimension del tensor 3d " ,tensor3d.ndim)
#agregar o eliminar dimensiones
#de esta manera desde que creamos un tipo de dato podemos darle las dimensiones que queramos
vector2=np.array([11,22,33],ndmin=5)
print(vector2,"dimensiones del vector " , vector2.ndim)

#ahorasi quire aumentarle una dimension a un dato usamos el sig

vectorAumentarDim=np.array([1,2,3])
vectorAumentarDim=np.expand_dims(vectorAumentarDim,axis=1) #al decirle axis 0 es como decirle
#aumenta una fila , y al decirle axis=1 es decirle aumenta una columna
print(vectorAumentarDim,"dimension vector " , vectorAumentarDim.ndim)

#ahora queremos eliminar la dimension qu no estamos usando por ejemplo del vecto2 que tiene 5
print(vector2,"dimensiones del vector2 " , vector2.ndim, "AHORA USARE LA FUNCION PARA ELIMINR LAS DIMENSIONES QUE NO USEMOS ")
vector2=np.squeeze(vector2)
print(vector2,"estas son las dimensiones que le quedan ", vector2.ndim)

