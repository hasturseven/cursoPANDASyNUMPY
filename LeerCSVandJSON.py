import pandas as pd

"""PODEMOS TENER VARIOS TIPOS DE ARCHIVOS A LEER PERO PARA LEERLOS LE PASAMOS LA ESTENCION EJEMPLO pd.read_txt en 
este caso usamos csv que es el que mas se usa y estamos leyendo el archivo que descargamos """
datos=pd.read_csv('datos/bestsellers-with-categories_e591527f-ae45-4fa5-b0d1-d50142128fa6.csv')
print(datos)

"""ahora tambien podemos tener otro separador en nuestro csv que sea talvez un / (slash) entonces se lo podemos 
idicar cpn el , sep='/' pero generalmente son , estas se ponen por defecto asi no las especifiquemos tambien el 
header es el nombre que tienen las columnas generalmente los archivos csv lo traen 
pero en el caso que no tengan nombre ponemos header=None cuando se ahce eso solo enumera las columnas  o si esta 
en otra columna ponemos header=4 que en este caso  estaria en la columna numero 4 y asi los rescata pero no me 
deja ver los datos anteriores la posicion por defecto es 0  """
datosSpotify=pd.read_csv('datos/spotify_dataset.csv',sep=',',header=0)
print(datosSpotify)

"""TAMBIEN PUEDO NOMBRAR LAS COLUMNAS COMO YO DESEE POR EJEMPLO LOARE CON EL DE SPOTIFY"""
"""si dejo sin renombar unas columnas me las dejara sin nomre y las unira con las que no les puse nombre entonces 
primero verificar que nombre todas las columnas para que no se presente mal la informacion """
columns_modificadas_spotify=pd.read_csv('datos/spotify_dataset.csv',sep=',',header=0,names=['numero de serire','cancion','artista','genero','duracion','disquera','pais','stream'])
#ahora con .colums me muestra el nombre de las columnas
names_columas=columns_modificadas_spotify.columns

print(columns_modificadas_spotify)
""" --------------------------------------------- AHORA LEYENDO JSON ----------------------------------------------"""
"""-----------------------------GENERALMENTE NO SE SUELE TRABAJR CON ESTOS ASI QUE SE LLEVAN ES A CSV --------------"""
#asi se leen los json
archivo_json=pd.read_json('datos/hpcharactersdataraw_3d934e85-dfa4-42ec-8520-fadfbecae574.json')
print(archivo_json)
""" AHORA PODEOS DECIRLE EL TIPO DE FORMATO QUE QUETAMOS PUEDE SER SERIES """

archivo_json_series=pd.read_json('datos/hpcharactersdataraw_3d934e85-dfa4-42ec-8520-fadfbecae574.json',typ='Series')


