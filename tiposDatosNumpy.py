import numpy as np

# de esta manera le especificamos un tipo de dato pasando el sregundo argumentpo
from numpy import ndarray

arr = np.array([1.222, 2, 3, 4], dtype='float64')

print(arr)

# !IMPORTANT_AHROA_LO_PODEMOS_AHCE"R_DE_OTRA_MANERA"  TODo depende como nos quede mejor hacerlo

arr2 = np.array([0, 1, 2, 34])
arr2 = arr2.astype(np.bool_)  # ahora estamos convirtiendo estos valores a booleanos
print(arr2)

# ahora convirtiendoles de entero a string
arr3 = np.array([0, 1, 2, 34])
arr3 = arr3.astype(np.string_)  # ahora estamos convirtiendo estos valores a booleanos
print(arr3, 'esa forma tan peculiar de imprimir indica que ya pasamos de entero a strgin ', arr3.dtype)
# ahora de texto a entero

arr4 = np.array(["0", "1", "2", "3", "4"]).astype(np.float16)
arr4 = arr4.astype(np.int32)  # ahora estamos convirtiendo estos valores a booleanos
print(arr4, "de esta manera convertimos todo de string a int de 32")
