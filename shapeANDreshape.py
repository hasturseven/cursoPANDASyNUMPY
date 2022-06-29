import numpy as np

# aca estoy creando un arreglo de 3 filas ,con 5 columnas , y cada fila dentro del arreglo tendra 2 filas
# el primer 3 es el de las filas mas general osea las de afuera
# el segundo 2 es que cada fila estara distribuida con 2 filas
# y el 5 son las columnas generales que se cumplen para todos
arr = np.random.randint(1, 10, (3, 2, 5))
print(arr)
# shape me dice como esta distribuido mi arreglo
print("el shape es como decirme cuantas filas y columnas tengo , mejror dicho cuantas dimensiones", arr.shape)
# el reshape me dice como quiero distribuir mi arreglo siempre y cuando se respete la cantidad de datos ej:
arr = np.random.randint(1, 10, (3, 2))
print(arr)
# ahora lo distribuiremos como tenemos 6 datos en total puedo decir que sea un vector de 6 datos ej IMPORTANTE
# SIEMPRE DEBERA SER DISTRIBUIIDO CON LA MISMA CANTIDAD DE DATOS QUE TENEMOS NO PUEDO DECIR QUE SEA (1,10: YA QUE NO
# TENGO 10 DATOS
print(arr.reshape(1, 6))

# o una matriz con 2 filas y 3 columnas
print(arr.reshape(2, 3))

# DE ESTA FORMA TAMBIEN SE PUEDE HACRE ES APLICABE PARA TODAS LAS FUNCIONES DE NUMPY ES LO MISMO QUE LO ANTERIPOR
# PERO PRESENTADO DE DIFERENTE MANERA
print(np.reshape(arr, (1, 6)))

# también le puedo decir que lo ordene como lo hacen LOS LENGUAJES EN ESPECIFICO POR EJEMPLO COMO LO HACE C O FORTRAN
# para hacer esta specified ES OBLIGATORIO USAR LA OTRA FORMA DE UAR LAS FUNCIONES EN NUMPY para que se vea mas
# claro presentaré cmo teníamos el arreglo
print()
print(arr)
print()
# yahora si aplicare la forma que quiero que lo muestre ES SIEMPRE MEJOR USAR CON C
print(np.reshape(arr, (2, 3), 'C'))
# EN C EL 2 REPRESENTA LAS FILAS Y EL 3 SERA MIS COLUMNAS SIEMPRE
print()
# ahora lo haremos que lo ordene como en fortran

print(np.reshape(arr, (2, 3), 'F'))

# ahora como lo presentaria fortran recordando que de esta manera me genera un error toca es usar np.reshape
# print(arr.reshape((2,3),'F'))

# ahora esto lo ara segun como este optimizado el guardado de datos en mi pc osea de donde le quede mas facil agarrar
# a mi ram disco duro etc..
print(np.reshape(arr, (2, 3), "A"))
# esto GENERALMENTE LO ARA COMO C PERO ES MEJOR HACERLO CON LA ORMA DE C YA UQE TENGO EL CONTROL DE LAS FILAS Y COLUMNAS


# --------------------resolviendo los retos-------------------------------------
print("resolviendo reto")
array3d = np.random.randint(1, 5, (3, 2, 4))
print(array3d)
# ahora cambiaremos la dimension con reshape
print("dimension actual ", np.shape(array3d))
print("ahora con la dimension cambiada ", np.reshape(array3d, (2, 2, 6)), " y sus dimensiones son ", np.reshape(array3d, (2, 2, 6)).shape)

print("haciendo el de no respetar estructura original")
array1d = np.random.randint(1, 5, 8)
print(array1d)
print(np.reshape(array1d, (2, -1)))
# al darle el menos uno el reshape se calculó de manera que se distribuya correctamente solo puedo usar un menos uno por
# dimension osea no puedo usar dos a la vez o tres solo uno
