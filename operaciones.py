import numpy as np
lista=[1,2]
print(lista)

print(lista*2) #me duplicara la lista
print("ahora usando numpy")

arr = np.arange(0,10)
arr2=np.copy(arr)

print(arr2*2,"al poner el arr2 * 2 me multiplica por 2 cada element de la lista")
print(arr2+2,"al poner el arr2 + 2 mesuma por 2 cada element de la lista")
print(arr2+2/arr,"al poner el arr2 / arr me divide la lista 2 por la 1 y en la posicion donde tengo un cero todos sabemos que dividir por cero es un error asi que esto no me generara un error si no que me dejara un nan o un inf continuando la ejecucion del programa pero luego si al final me muestra el error mas bien u nwarning ")
print()
print()
print("ahora podremos hacer operaciones dentro del array osea por cada posicion asi")
arrOperaciones=arr+(arr2+2)
print("con suma" ,arrOperaciones)
print()
arrOperaciones=arr-(arr2+2)
print("con resta",arrOperaciones)
print()
arrOperaciones=arr*(arr2+2)
print("con multiplicacion",arrOperaciones)
print()
arrOperaciones=arr**(arr2+2)
print("con elevar",arrOperaciones)
print()
print("ahora trabajando con matriz es lo mismo ejemplo , PERO CON EL PRODUCTO PUNTO Y TAMBIEN DEBE HABER PRODUCTO CRUZ")
print("TENEMOS EL IMPORTANTE PRODUCTO PUNTO")
matriz=arr.reshape(2,-1)
matriz2=matriz.copy()
print("aplicando el producto punto")
print(np.matmul(matriz,matriz2.T),"asi queda el producto punto se puso la transpuesta de la dos ya que para el producto punto se multiplican ambas matrizes osea la fila1 de la matriz por la columna de la matriz2")
print("otra manera de hacer el producto punto es con matriz @ matriz2.T el arroba es como decirle el producto punto de esas dos")

productoPuntoDeOtraForma=matriz @ matriz2.T

print(productoPuntoDeOtraForma)

print()
print(matriz)
print()
print(matriz+matriz2,"ahora sumando posicion por posicion de las matrices")
print()
print(matriz-matriz2,"ahora restando posicion por posicion de las matrices")

print("no olvidar que el warning que aparece es de  la posicion que se dividio por cero algunas veces aparece arriba otras abajo y asi...")