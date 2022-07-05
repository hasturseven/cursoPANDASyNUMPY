import  pandas as pd

df_books=pd.read_csv('datos/bestsellers-with-categories.csv')
print(df_books.head(4))

#ahora vamos a filtrar por condiciones y nos retornara true o false

mayor_2016=df_books['Year']>2016
print(df_books['Year']>2016)
#ahora vamos a mostrarlos
print(df_books[mayor_2016])

#ahora filtrando por genero fiction de la forma reducida que es meter la condicion dentro del df_books pero mejor es usando variables

generoFiccion=df_books['Genre']=='Fiction'

print(df_books[generoFiccion & mayor_2016])

#ahora si quier filtrar los que sean menores a 2016 simplemente uso la expresion negacion y listo en pandas TENEMOS QUE USAR EL ~ PARA QUE ME HAGA LA NEGACION

print(df_books[generoFiccion & ~mayor_2016])
#FILTRANDO CON TEXTO USANDO LA FUNCION STR.CONTAINS()


print(df_books[df_books['Author'].str.contains('Palacio')])