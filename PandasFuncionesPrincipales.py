import pandas as pd

df_books = pd.read_csv('datos/bestsellers-with-categories.csv')

print(df_books.head(3))

"""EL INFO() ES EXCELENTE MEM MUESTRA LAS COLUMNAS CON SUS NOMBRES ME DICE CUANTOS INDEX TENGO ES DECIR CUANTAS FILAS 
TAMBIEN ME DICE EL TIPO DE DATO QUE ESTOY MANENAJANDO TAMBIEN CUANTOS DATOS SON NO NULOS Y MAS INFOR DEMACIADO 
IMPORTANTE SIEMPRE USARLO """
print(df_books.info(), 'mostrando informacion muy importante')
""" PARA OPTIMIZAR ESTE ES MUY UTIL .memory_usages osea me dice cuanta memoria estoy consumiendo"""
print()
print(df_books.memory_usage(deep=True), 'mostrando la memoria usada por filas columanas etc')
print()
"""el .DESCRIBE() A NIVEL DE CIENCIA DE DATOS ES MUY UTIL POR QUE A PARTIR DE LOS DATOS NUMERICOS ME DA LA MODA LA 
MEDIANA LA MINIMA EL 50% ETC EN TONCES ES MUY UTIL PARA USARLA PARA MANEJO DE NUMEROS ETC """
print()
print(df_books.describe(), 'mostrando la media etc.. de los datos numericos del dataframe')
print()
print()
""".tail(2) nos sirve para que me muestre los ultimos datos es decir lo mismo que head pero lo hace es ocn las colas  """
print()
print(df_books.tail(8), 'mostrando los ultimos 8 registros')
print()

"""value_counts me cuenta la repeticiones que encontremos en la columna en este caso sera columnas por que le pasamos columnas """
print()
print(df_books['Author'].value_counts(), 'mostrando cuantas veces se repiten los autores')
print()

"""PARA LIMPIAR EL DATASET USAMOS EL DROP_DUPLICATES EL CUAL ELIMINA LOS REGISTROS DUPLICADOS tambien le podimos 
decir cual dejar digamos el ultimo duplicado osea el ultimo ingresado o dejarlo solo y deja es el primero """
print()
print(df_books.drop_duplicates(keep='last'),
      'borrando los duplicados osea borra los datos que sean exactamente ogual osea que todas las columnas esten llenas igualmente')
print()

""".sort_values  ME SIRVE PARA ORDENAR LOS DATOS COMO ME VENGAN EN GANA"""
print()
print(df_books.sort_values('Year', ascending=False))
print()
