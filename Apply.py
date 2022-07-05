# apply sirve para dejar usar funciones que creemos en python para aplicarlas a los dataframes

import pandas as pd

df_books = pd.read_csv('datos/bestsellers-with-categories.csv')

print(df_books.head(2))


def two_times(values):
    return values * 2

#aca usamos la funcion apply para pasarle la funcion de python y como se que del user rating yo recibo un valor por eso en la palicacion de python puse values pero al hacer el llamado no hace falta ponerle los parentesis
df_books['Creando User Rating 2'] = df_books['User Rating'].apply(two_times)

print(df_books.head(4))

#ahora aplicando funciones lambda
df_books['Creando User Rating con lambdas'] = df_books['User Rating'].apply(lambda x:x*3)
print(df_books.head(3))

#usando distintas columnas para hacer operaciones
#en este caso aplicaremos la funcion lambda a todos el data frame entonces EL VALOR DE X COMO ESTAMOS TOMANDO EL DATA FRAME COMPLETO TOMARA TODAS LAS FILAS Y EL VALRO PARA CADA COLUMNA
#el axis es que le estamos diciendo que tome como referencia las columnas para que entienda los nombres como genre etc...

df_books['lambda para todo el data frame']=df_books.apply(lambda x: x['User Rating']*2 if x['Genre'] == 'Fiction' else  x['User Rating'],axis=1)

print(df_books.head(7))
