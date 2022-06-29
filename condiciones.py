import numpy as np

arr=np.linspace(1,10,10,dtype='int8')
print(arr)
#al hacer esto le estoy diciendo quienes son mayores a 5 asique me mostrara una lista con booleans si cumple la condicion me dara tur del resto me dara false
print(arr>5)

#ahora guardare los resultados en una vriable
indices_condicion=arr>5
print(indices_condicion)
#como vemos me guarda lso estados booleanos
print()
print("ahora si yo quiero que me imprima la lista con la condicion de lso valores mayores a 5 puedo hacer lo sig")
print()
print("al poner la otra lista dentro de la lista principal me imprimira solo los true que son los mayoresa 5")
print(arr[indices_condicion])
print(arr[arr>5] ,"como vemos tambien logro lo mismo de esta manera ")

#tambine puedo hacer uso de las expresiones egulares como el and or o not osea | & !
print(arr[((arr>5) & (arr<9))] , "de esta manera solo esta imprimiendo los mayores 5 y menores que 9")


