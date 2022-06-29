import numpy as np
arr=np.arange(0,11)
print("el arreglo original",arr)

trozo_arr= arr[:6]
print("trozo de arreglo original sin operar " ,trozo_arr)
print("aca creamos un otra variable con un trozo de arreglo y la operamos para que esa variable trozo de arreglo sean ceros")
trozo_arr[:]=0 #dejando todos el trozo en 0

print("ahora imprimiremos el arreglo original ", arr, "y ahora el trozo ", trozo_arr,"como se puede ver dañamos el arreglo principal apezar que lo teniamos en otra variable por eso debemos usar el copy")
print()

print("ahora trabajando con el np.copy que es el que no me deja que se dañe el original")

arr2=np.arange(0,11)
arr_copy=np.copy(arr2[:8])
print("arreglo usando el copy",arr_copy)
print("ahora al usar el copy no me dañara el anterior con el arr_copy le dare a todos valores de 100")

arr_copy[:]=100

print("ya le asigne a todo el arr_copy valores de 100")
print("ahora imprimire el arreglo original ",arr2," y ahora el arreglo copy modificado" , arr_copy)
