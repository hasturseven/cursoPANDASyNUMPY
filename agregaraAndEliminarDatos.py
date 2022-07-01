import pandas as pd
import numpy as np


def funcionAumentaIndex(posicionIndex):
    print(type(posicionIndex))
    return posicionIndex+1
"""---------------- CARGANDO EL ARCHIVO PARA HACER EL AGREGADO O ELIMINACION DE 
DATOS LAS COSAS QUE SE AGREGUEN O ELIMINEN NO SE VERA NAFECTADAS EN EL DATA FRAME ORIGINAL 
------------------------------------------ """
music_spoty = pd.read_csv('datos/spotify_dataset.csv')
PROBANDOalgo = pd.read_csv('datos/bestsellers-with-categories.csv')

# ------------------- eliminando columnas-----------------------------
# ESTA FUNCION ME MUESTRA LAS PRIMERAS 5 lineasDEL DATAFRAME
print(music_spoty.head())

# ESTA FUNCION ELIMINARA LAS COLUMNAS DE SALIDA (osea cuando lo imprima) PERO NO DEL DATAFRAME OSEA DEL ARCHIVO lo
# guardare en variables para que sea facil de visualizar
# SI PONGO MAL EL EJE ME GENERARE ERRO ENTONCES ENGO QUE RECORDAR QUE LOS NOMBRES ESTAN EN EL EJE 1 QUE EN ESTE CASO SERIA NUESTRAS COLUMNAS Y EL EJE 0 SON LAS FILAS

imprimirSinColumnaEspecifica = music_spoty.drop('Song', axis=1).head()
# imprimirSinColumnaEspecifica=music_spoty.drop(range(0,3),axis=1).head()
# PUEDO HACER USO DEL RANGE SIEMPRE Y CUANDO EL NOMBRE DE LAS COLUMNAS ESTEN IDEZADAS DE LO OCNTRARIO ME TOCA PONR EL NOMBRE

print(imprimirSinColumnaEspecifica)

# ELIMINANDO COLUMNA DEL DATAFRAME ; PARA NO ALTERAR MI ARCHIVO LO ARE DE ACTUALMUSIC

"""LA MEJOR MANERA DE BORRAR ES CON el drop DE ARRIBA pero debo pasar correcto el axis y agregarle el inplace=TRUE"""

# y de esta manera es correcto borrar datos hacemos la que mas nos guste a este drop tambien le podemos meter el range(0,6) pero para ejes nombrado toca poner los nombres
music_spoty.drop('Genres', axis=1, inplace=True)
print(music_spoty.columns, "COMO PODEMOS VER YA NO ESTA Genres YA QUE USE EL OCMANDO APRA ELIMINARLO")  # ahora
# mostrando que borramos el Genres

"""otra manera de borrar es usando el del no da tantas opciones pero es buena para eliminar columnas que esten 
nombradas """
del music_spoty['Song']

print(music_spoty.columns, "COMO PODEMOS VER YA NO ESTA SONG YA QUE USE EL OCMANDO APRA ELIMINARLO")  # asi solo
# muestra los dos primeros datos o la cantidad que le pasemos
print()

print()
print("PODEMOS USAR LA OPCION QUE QUERAMOS MEJOR DICHO LA QUE MEJOR SE ACOMODE ")
print()

# ------------------------------ eliminando filas ---------------------------

# s aplican los mismos casos pero para el otro lo uno que cambia es el eje que ya sera 0 (por uqe estaremos haciendo referencia a las filas) tambien puede recibir tuplas
# ya que las filas siempre estan indezadas , RECORDAR SI QUIERO QUE SE BORREN DEL DATAFRAME TENGO QUE PONER EL INPLACE=TRUE EN ESTE CASO NO HACE FALTA

print(music_spoty.drop(range(0, 3), axis=0).head(3),
      "como se observa inica desde la fila 3 ya uqe la 0 , 1,2 las elimino ")

del music_spoty['Serial Number']

print(music_spoty.head(10))

# -------------------------AHORA AGREGAR COLUMNAS------------------------------------
# EL NP.NAN ES QUE LE AGREGA VALORES TEXTUALES QUE SON NAN OSEA VACIOS APARECERAN OCMO NAN
# o puedo poner zeros como son 170 filas le tendre que pasar 170 ceros
music_spoty['nueva_columa_zeros'] = np.zeros(170)
music_spoty['columna nan'] = np.nan

print(music_spoty.head(10),
      "y como se puede observar si se agregaron las columnas el problema es que siempre se deben rellenar")

print(music_spoty.shape[0], "esto me imprime la cantidad de filas que serian la cantidad de datos que tengo el dataset")

# ya sabiendo esto que el .shape[0] me da la cantidad de datos puede hacer un array que lo llame rango y se le asige ej
music_spoty['rango'] = np.arange(0, music_spoty.shape[0])
print(music_spoty.head(10),
      "y como se puede observar si se agregaron las columnas el problema es que siempre se deben rellenar completamente por eso usamos el shape para saber cuantos datos son ")

# ---------------------AHORA AGREGANDO FILAS-------------------------------------
# Existen muchas formas de hacerlo pero la recomendada por pandas es concat asi que vamos a usarla

# para usar concact es como los string que solo concatenaba string este caso sera similar tengo que pasarle una serie o un data frame
#entonces si estoy manejando una serie paso otra serie pero en este caso me toca pasar otro data frame le debo pasar el nombre de las columnas para que sea igual y lo ingrese en el lugar correcto, tambien puede resibir diccionarios

columnas=music_spoty.columns

dataIngresar = pd.DataFrame([[1,2,3,4,5,6,7,8,17],[9,10,11,12,13,14,15,16,19]],columns=columnas)
#el ignorar index sirve para que siga el index del primero osea de music_sopty ya que o sino pasara con el index del data que yo cree
music_spoty=pd.concat([music_spoty, dataIngresar],ignore_index=True)

print(music_spoty)

""" tambien podemosde esta manera pero tenemos que sber el ultimo index para eso usamos el .shape y pasamos los valores tamien podemos usar diccionarios"""
listaDat=['sergio','el','mas','ca','po','1','3','3','4']
music_spoty.loc[funcionAumentaIndex(music_spoty.shape[0])]=listaDat
music_spoty.loc[funcionAumentaIndex(music_spoty.shape[0])]=listaDat
music_spoty.loc[funcionAumentaIndex(music_spoty.shape[0])]=listaDat


