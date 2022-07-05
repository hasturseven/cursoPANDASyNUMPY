import pandas as pd
import numpy as np
# creando mi propio data frame
diccionario = {'A': ['A1', 'A2', 'A3'],
               'B': ['B1', 'B2', 'B3'],
               'C': ['C1', 'C2', 'C3'],
               'D': ['D1', 'D2', 'D3']}

df1 = pd.DataFrame(diccionario)
diccionario2 = {'A': ['A4', 'A5', 'A6'],
                'B': ['B4', 'B5', 'B6'],
                'C': ['C4', 'C5', 'C6'],
                'D': ['D4', 'D5', 'D6']}
df2 = pd.DataFrame(diccionario2)

"""AHORA MANIPULANDO LOS DATA FRAME PAA HACER EL USO DE MERGE Y CONCAT"""

#AHORA USAREMOS EL CONCAT PARA UNIRLOS ahora para ignoe index para que sea secuencial el index por default el l hace por axis cero que son las filas
nuevoDataFramesFilas=pd.concat([df1,df2],ignore_index=True)
print(nuevoDataFramesFilas)

#ahora quiero que sea con las columnas pero es raro hacerlo de esta manera asi que generalmente se le hace por filas para las columnas ponemos axis=1

nuevoDataFramesColumnas=pd.concat([df1,df2],axis=1)
print(nuevoDataFramesColumnas)

"""---------------------------USO DEL MERGE SIRVE PARA FILAS----------------------"""
diccionarioMerge={'key':['k1','k2','k3'],
                  'A': ['A1', 'A2', 'A3'],
                  'B': ['B1', 'B2', 'B3']
                  }

df_izq=pd.DataFrame(diccionarioMerge)
diccionarioMerge2={'key':['k1','k2','k3'],
                  'C': ['C1', 'C2', 'C3'],
                  'D': ['D1', 'D2', 'D3']
                  }
df_der=pd.DataFrame(diccionarioMerge2)


"""------ MODIFICANDO UN POCO EL DATA FRAME PARA ESPECIFICARLE SOBRE CAL COLUMNA YA QUE VAN A TENER COLUMNAS DIFERENTES"""
df_izq=pd.DataFrame(diccionarioMerge)
diccionarioMerge2={'key_2':['k1','k2','k3'],
                  'C': ['C1', 'C2', 'C3'],
                  'D': ['D1', 'D2', 'D3']
                  }
df_der=pd.DataFrame(diccionarioMerge2)

"""USANDO EL MERGE EN ESTA OCACION USANDO LA COMBINACION"""
combinacionDifColm=df_izq.merge(df_der,left_on='key',right_on='key_2')
print(combinacionDifColm)

"""MODIFICANDO EL DERECHO PARA DEJARLE UN VALOR EN NAN si tengo el valor en nan me eleiminara la fila 3 en ambos asi que usaremos en how para decirle cual es el que tiene prioridad y que traga esos datos  """

diccionarioMerge2={'key_2':['k1','k2',np.nan],
                  'C': ['C1', 'C2', 'C3'],
                  'D': ['D1', 'D2', 'D3']
                  }
df_der=pd.DataFrame(diccionarioMerge2)
combinacionConNan=df_izq.merge(df_der,left_on='key',right_on='key_2')
print(combinacionConNan)
print()
print("AHORA USANDO EL HOW ARA DECIRLE CUAL TENDRA PRIORIDAD Y QUE ME TRAIGA ESA FILA CON SUS DATOS CORRECTOS EN ESTE CASO SERA LA IZQ")

combinacionConNan=df_izq.merge(df_der,left_on='key',right_on='key_2',how='left')
print(combinacionConNan)
print()
print("como podemos ver si me trajo los datos de la izquierda pero los de la derecha me los deja en nan")
print()
print("ahora con el de la derecha")
combinacionConNan=df_izq.merge(df_der,left_on='key',right_on='key_2',how='right')
print(combinacionConNan)