import pandas as pd

# leyendo el archivo csv
df_books = pd.read_csv('datos/bestsellers-with-categories.csv')
print(df_books.head(2))

"""AHORA CREAREMOS UN AGRUPAMIENTO SENCILLO CON GRUOBY para que cuente los registros por autor"""
agrupamientoSencillo=df_books.groupby('Author').count()
print(agrupamientoSencillo)
print()
"""AHORA LO AGRUPAMOS Y SUMAMOS REWIEWS CON REVIEWS ES DECIR CUANTAS VECES SE REPITA SE SUMARA ENTRE SI LOS CAMPOS 
POR ESO EN YEAR APARECE 4025 RECORDEMOS QUE LOC ES BUSQUEDA POR ETIQUETA ENTONCES BUSCARA LOS AUTORES CON EL NOMBRE 
QUE LE PASAMOS """
print("ahora le dire que me sume todos los campos en odnde aparezcan william dabis")
print(df_books.groupby('Author').sum().loc['William Davis'])
print()

"""como podemos ver el autor paso a ser el index en la primera vez que imprimimos la tabla entonces si queremos que 
el autor no sea el index y sea tomado cmo columna mas y me indexe los valores que me retorne usamos el reset index """

print()
print(df_books.groupby('Author').sum().reset_index(),'\n nos sirve usar el index como para mostrar en total la cantidad de autores y asignarles como un valor como se puede ver ')
print()

""".agg es indicarle que haremos determinadas funciones de agregagacion es decir darle ciertos parametros mas para 
que me muestre no se talvez muestrame el minimo  maximo de cada campo para cada valor porejemplo pra price me muestra o meterle 3  o mas cmapossegun lo que nos sea conveniente
el valor minimo y luego el max del libro etc.... """
print()
agrupacionTresVariables=df_books.groupby('Author').agg(['min','max','sum']).reset_index()
print(agrupacionTresVariables,'\n de esta manera le estoy pidiendo que me de el minimo y el maximo para cada columna ejemplo el año etc..')

print()

"""ahora lo puedo ser mas esecifico diciendole quiero trabajar solo con los reviews y el user rating pero que del user rating quiero solo la suma y asi"""
print()
busquedasMasPersonalizadas=df_books.groupby('Author').agg({'Reviews':['min','mean'],'User Rating':'std'})
print(busquedasMasPersonalizadas)

#"""ahora los agrupare por author y year y ahora estos pasan a ser una llave compuestra"""
agrupandoPorDosVariables=df_books.groupby(['Author','Year']).count()
print(agrupandoPorDosVariables)

