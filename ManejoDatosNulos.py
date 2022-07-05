# ESTO ES MUY IMPORTANTE YA QUE SE ENCONTRARAN MUCHOS DATOS NULOS Y TENEMOS QUE MANEJARLOS  BIEN
import numpy as np
import pandas as pd

diccionario = {'Col1': [1, 2, 3, np.nan],
               'Col2': [4, np.nan, 6, 7],
               'Col3': ['a', 'b', 'c', None]}

df_datos=pd.DataFrame(diccionario)

print(df_datos)

#AHORA USAMOS LA FUNCION .ISNULL() PARA QUE ME DIGA QUE VALORES SON NAN O NONE OSEA QUE SON NULOS Y ME COMPLICA EL MANEJO DE DATOS me dara un arreglo con true y false

print(df_datos.isnull())

"""LO QUE GENERALMENTE HACEN LOS CIENTIFICOS DE DATOS CUANDO TIENEN DATOS NULOS ES ELIMINAR ESAS FILAS ASI TENGA SOLO UN DATO NULO YA QUE MUCHAS VECES LOS NULOS SON POCOS DATOS Y NO AFECTA TENER EN CUENTA ESAS COLUMNAS LO UQE SE USA ES dropna() recorando que primero se hace el isnull() para saber cuales son nulos identificacion y completarlos usamos lo de abajo"""

borrandoLosDatosNulos=df_datos.dropna()
print(borrandoLosDatosNulos)

# PERO LA MEJOR MANERA DE MANEJAR ESTOS TIPOS DE DATOS NULOS ES PRESENTARLOS CON 0 Y 1 (LOS CEROS SON LOS DATOS NO
# NULOS Y EL 1 SON LOS DATOS NULO) o DECIRLE QUE LE PONGA MISSING EL QUE ME PAREZCA MAS COMOdo LO MEJOR ES USAR
#TAMBIEN PUEDO USAR INTERPOLATE() QUE TRATARA DE SEGUIR EL PATRON O LA SERIE QUE VEA EN NUMEROS EN TEXTO NO SIRVE
# fillna() YA QUE PUEDO VER TAMBIEN LOS DATOS

datosMissing=df_datos.fillna('Missing')

print(datosMissing)
print()

#TAMBIEN PUEDE DIRLE QUE LO LLENE CON LA MEDIA LA MODA LO QUE SEA PERO PARA LOS QUE TENGA DATOS TECTUALES SERA AGREGARLE OTRA COSA COMO LA MODA

datosMissing=df_datos.fillna(df_datos.mean())

print(datosMissing)
print()
print("ahora usando la moda si me rellenara hasta los de texto , PERO ISN O TENEMOS MODA PARECERA IGUAL")
datosMissing=df_datos.fillna(df_datos.mode())
print(datosMissing)
print()
print("AHORA SI USO INTERPOLATE Y MANEJO NUMEROS TRATARA DE SEGUIR COMO ESA SERIE O PATRON PARA TEXTO NO SIRVE")
datosInterpolados=df_datos.interpolate()
print(datosInterpolados)
print()
print("AHORA MOSTRANDOLOS CON 0 Y 1 USAR EL QUE M CONVENGA MAS")

datosNulos=df_datos.isnull()*1

print(datosNulos)

