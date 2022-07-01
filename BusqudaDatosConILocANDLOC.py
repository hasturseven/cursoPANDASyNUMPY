from _ast import mod

import pandas as pd

"""---------------- CARGANDO EL ARCHIVO PARA HACER EL FILTRADO------------------------------------------"""
music_spoty=pd.read_csv('datos/spotify_dataset.csv')
print(music_spoty)#darle en wiew as dataframe que aprarece al lado del nombre de la variable cuando se ejecuta en consola
"""-------------USANDO LOC , LOC SIEMPRE FILTA USANDO LABELS OSEA EQUITETAS"""
#de esta manera mostraremos todos usando loc
print(music_spoty.loc[:])
#AHORA MOSTRAREMOS DESDE EL INICO HASTA LA POSICION 4 Y QUE SOLO MUESTRE EL NOMBRE DE LA CANCION Y EL ARTISTA }
print(music_spoty.loc[0:4,'Song'])


#modificando una columna especifica en este caso multiplicamos la duracion generando duraciones negativas al multiplicarla por -1

print(music_spoty.loc[:,['Song']] + "lol")

#ahora filtrando datos con una condicion que yo determine por ejemplo que el serial sea menor o igual a 16
print(music_spoty.loc[:,['Serial Number']]<= 16)

"""----------------------------usando ILOC PARA FILTAR , ILOC SOLO FILTRA USANDO LOS INDICES TAMBIEN PUEDO HACER LO 
MSMO QUE EN LOC COMO CONDICIONES ETC .... SI NO QUE ESTE SE AHCE CON INDICES ----------------- """
print(music_spoty.iloc[:]) #mostrando todos el contenido
#filtrando los datos segun el indice de las filas y columnas
"""EN ESTE CASO MOSTRARA LOS DATOS DE LAS FILAS QUE VAN DE 0 A 3 , Y LAS COLUMNAS SOLO 0 Y 1"""
print(music_spoty.iloc[:4,0:2])
#MOSTRANDO UN DATO ESPECIFICO Y MODIFICNADOLO en el serial number
print(music_spoty.iloc[3,0]*-1 ,"este es el serial number modificado")

"""--------------------------AL MODIFICAR UN DATO NO SE VERA EN MI CSV ORIGINAL ----------------------------"""






print()
print()
print()
print("RECORDAR QUE ESTA FORMA NO ES CONVENIENTE HACERLA")
print()
#PODEMOS USAR SLICING PARA HACER FILTRADO PERO ES MEJOR USAR LOC O ILOC PARA FILTAR
print(music_spoty[0:4],"mostrando datos usando sliceing mejor es usar loc y iloc")
print(music_spoty[['Song','Artist']],"mostrando datos usando sliceing mejor es usar loc y iloc")


