"""PIVOT Y MELT SON Funciones que nos sirven Para cambiar la estructira de nuestro dataFrame de acuerdo a nuestras
necesidades """
import pandas as pd
#cargando el data frame
df_books = pd.read_csv('datos/bestsellers-with-categories.csv',sep=',',header=0)
#ahora presentando las primeras 5 lineas
print(df_books.head())
#aplicando el pivot
print()
pivot=df_books.pivot_table(index='Author',columns='Genre',values='User Rating')
# Como resultado, los valores de Author pasan a formar el índice por fila y los valores de Genre pasan a formar parte
# de los índices por columna, y el User Rating se mantiene como valor. basicamente esto me da que para al decir
# indice es ocmo seleccionar el nombre del autor como una llave principal osea como el indentificador por que para
# cada uno de ellos vamos a presentar las labores ahora las columnas seran las que tengamos en genero es decir los
# valores que se manejan en generos que en este caso es fiction y non fiction para este caso tendremos 2 columnas Y
# AHORA LO QUE LLENARA ESTAS COLUMNAS PARA CADA AUTOR EN ESPECIFICO QUE ES EL INDEX SERA EL DATO QUE PASAMOS COMO VALUES QUE ES EL USER RATING
print(pivot)

#Por supuesto, para este caso, un Author suele tener un solo género literario, así que no es una transformación muy útil, pero veamos si podemos lograr algo mejor.

#ahora la aggfunc sirve para que sume el uer rating por año tambien podemos pasarle la moda o el std etc...
print()
pivot_mejorado=df_books.pivot_table(index='Genre',columns='Year', values='User Rating',aggfunc='sum')
print()
#En este caso tenemos por cada género, la suma a lo largo de los años. Esto es mucho más interesante, ¿verdad? La mejor noticia es que no solo podemos obtener la suma, también podemos obtener la media, la desviación estándar, el conteo, la varianza, etc. Únicamente con cambiar el parámetro aggfunc que traduce función de agrupamiento.
print(pivot_mejorado)
print()
"""------------------------MELT-----------------------------------------"""
#El método melt toma las columnas del DataFrame y las pasa a filas, con dos nuevas columnas para especificar la antigua columna y el valor que traía.

#Por ejemplo, simplemente al imprimir las cinco primeras filas del DataFrame con las columnas de Name y Genre se tiene este resultado.
print()
print(df_books[['Name','Genre']].head(5))
print()
#ahora aplicando melt
usandoMelt=df_books[['Name','Genre']].head(5).melt()
print(usandoMelt)
print()
#Ahora cada resultado de las dos columnas pasa a una fila de este modo a tipo llave:valor.
"""----- ejecutando melt para que ignore una columna y no me presente ese dato pero si lo asocie con la variable uqe 
si quiero que forme la clave valor ------------- """

melt_condicionado=df_books.melt(id_vars='Year',value_vars='Genre')
#Simplemente, podemos seleccionar las columnas que no quiero hacer melt usando el parámetro id_vars. Para este caso Year y también la única columna que quiero aplicar el melt, para este caso Genre con la propiedad value_vars.
#osea basicamente asociara year con la columna principal pero no me la dara como clave valor si no qu genre sera la que tendra clave valor